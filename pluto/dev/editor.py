from pluto.utils import stream

from protos import development_pb2_grpc as dev_rpc
from protos import development_pb2 as dev
from protos import data_pb2


class Editor(dev_rpc.EditorServicer):
    def __init__(self, directory):
        '''

        Parameters
        ----------
        directory: pluto.interface.directory.AbstractDirectory
        '''
        self._directory = directory
        self._loop = None

    def New(self, request, context):
        with self._directory.write() as d:
            stg = d.add_strategy(request.name)
            response = dev.NewStrategyResponse(
                strategy_id=stg.id,
                template=next(stg.get_implementation(-1)))
            return stream.chunk_bytes(response.SerializeToString())


    def GetStrategy(self, request, context):
        '''

        Parameters
        ----------
        request
        context

        Returns
        -------
        typing.Generator
        '''
        with self._directory.read() as d:
            stg = d.get_strategy(request.strategy_id)

            for b in stg.get_implementation():
                yield data_pb2.Chunk(data=b)

    def Save(self, request_iterator, context):
        # todo: if a strategy is locked, then copy it and create a new id for this
        # strategy, so that we don't overwrite the locked strategy
        with self._directory.write() as d:
            buffer = b''
            for chunk in request_iterator:
                buffer += chunk.data
            stg = dev.SaveRequest()
            stg.ParseFromString(buffer)
            s = d.get_strategy(stg.strategy_id)
            try:
                s.store_implementation(stg.strategy)
            except RuntimeError:
                ns = d.add_strategy(s.name)
                ns.store_implementation(stg.strategy)
