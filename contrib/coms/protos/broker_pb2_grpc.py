# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from contrib.coms.protos import assets_pb2 as contrib_dot_coms_dot_protos_dot_assets__pb2
from contrib.coms.protos import broker_pb2 as contrib_dot_coms_dot_protos_dot_broker__pb2
from contrib.coms.protos import data_bundle_pb2 as contrib_dot_coms_dot_protos_dot_data__bundle__pb2
from contrib.coms.protos import finance_pb2 as contrib_dot_coms_dot_protos_dot_finance__pb2
from contrib.coms.protos import protocol_pb2 as contrib_dot_coms_dot_protos_dot_protocol__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


class BrokerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SingleOrder = channel.unary_unary(
        '/Broker/SingleOrder',
        request_serializer=contrib_dot_coms_dot_protos_dot_broker__pb2.OrderParams.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Order.FromString,
        )
    self.PortfolioState = channel.unary_unary(
        '/Broker/PortfolioState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Portfolio.FromString,
        )
    self.PositionsState = channel.unary_stream(
        '/Broker/PositionsState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.AssetPositionPair.FromString,
        )
    self.Transactions = channel.unary_stream(
        '/Broker/Transactions',
        request_serializer=google_dot_protobuf_dot_timestamp__pb2.Timestamp.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_finance__pb2.Transaction.FromString,
        )
    self.AccountState = channel.unary_unary(
        '/Broker/AccountState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Account.FromString,
        )
    self.BatchOrder = channel.unary_stream(
        '/Broker/BatchOrder',
        request_serializer=contrib_dot_coms_dot_protos_dot_broker__pb2.BatchOrderParams.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Order.FromString,
        )
    self.CancelOrder = channel.unary_unary(
        '/Broker/CancelOrder',
        request_serializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Order.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CancelAllOrdersForAsset = channel.unary_unary(
        '/Broker/CancelAllOrdersForAsset',
        request_serializer=contrib_dot_coms_dot_protos_dot_assets__pb2.Asset.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_broker__pb2.WarningMessage.FromString,
        )
    self.GetDataBundle = channel.unary_stream(
        '/Broker/GetDataBundle',
        request_serializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Domain.SerializeToString,
        response_deserializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Bundle.FromString,
        )


class BrokerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SingleOrder(self, request, context):
    """This should encapsulate the set of services available per account...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PortfolioState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PositionsState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Transactions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccountState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelAllOrdersForAsset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDataBundle(self, request, context):
    """bundle data is requested per account...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BrokerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SingleOrder': grpc.unary_unary_rpc_method_handler(
          servicer.SingleOrder,
          request_deserializer=contrib_dot_coms_dot_protos_dot_broker__pb2.OrderParams.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Order.SerializeToString,
      ),
      'PortfolioState': grpc.unary_unary_rpc_method_handler(
          servicer.PortfolioState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Portfolio.SerializeToString,
      ),
      'PositionsState': grpc.unary_stream_rpc_method_handler(
          servicer.PositionsState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.AssetPositionPair.SerializeToString,
      ),
      'Transactions': grpc.unary_stream_rpc_method_handler(
          servicer.Transactions,
          request_deserializer=google_dot_protobuf_dot_timestamp__pb2.Timestamp.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_finance__pb2.Transaction.SerializeToString,
      ),
      'AccountState': grpc.unary_unary_rpc_method_handler(
          servicer.AccountState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Account.SerializeToString,
      ),
      'BatchOrder': grpc.unary_stream_rpc_method_handler(
          servicer.BatchOrder,
          request_deserializer=contrib_dot_coms_dot_protos_dot_broker__pb2.BatchOrderParams.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Order.SerializeToString,
      ),
      'CancelOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CancelOrder,
          request_deserializer=contrib_dot_coms_dot_protos_dot_protocol__pb2.Order.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CancelAllOrdersForAsset': grpc.unary_unary_rpc_method_handler(
          servicer.CancelAllOrdersForAsset,
          request_deserializer=contrib_dot_coms_dot_protos_dot_assets__pb2.Asset.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_broker__pb2.WarningMessage.SerializeToString,
      ),
      'GetDataBundle': grpc.unary_stream_rpc_method_handler(
          servicer.GetDataBundle,
          request_deserializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Domain.FromString,
          response_serializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Bundle.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Broker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BrokerListenerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Update = channel.unary_unary(
        '/BrokerListener/Update',
        request_serializer=contrib_dot_coms_dot_protos_dot_broker__pb2.BrokerState.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class BrokerListenerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BrokerListenerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=contrib_dot_coms_dot_protos_dot_broker__pb2.BrokerState.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'BrokerListener', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
