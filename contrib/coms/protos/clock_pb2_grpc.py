# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from contrib.coms.protos import clock_pb2 as contrib_dot_coms_dot_protos_dot_clock__pb2


class ClockStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Sync = channel.unary_stream(
        '/Clock/Sync',
        request_serializer=contrib_dot_coms_dot_protos_dot_clock__pb2.SyncRequest.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_clock__pb2.SyncReply.FromString,
        )
    self.Delay = channel.unary_unary(
        '/Clock/Delay',
        request_serializer=contrib_dot_coms_dot_protos_dot_clock__pb2.DelayRequest.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_clock__pb2.DelayReply.FromString,
        )


class ClockServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Sync(self, request, context):
    """A service for clock synchronization... The client sends a sync request, the server
    returns two SyncReply messages, the client and server saves their local timestamp of the first sync reply.
    The server sends the timestamp of the follow-up message and the client uses it to compute the time difference.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delay(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClockServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Sync': grpc.unary_stream_rpc_method_handler(
          servicer.Sync,
          request_deserializer=contrib_dot_coms_dot_protos_dot_clock__pb2.SyncRequest.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_clock__pb2.SyncReply.SerializeToString,
      ),
      'Delay': grpc.unary_unary_rpc_method_handler(
          servicer.Delay,
          request_deserializer=contrib_dot_coms_dot_protos_dot_clock__pb2.DelayRequest.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_clock__pb2.DelayReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Clock', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
