# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import clock_pb2 as protos_dot_clock__pb2
from protos import controller_pb2 as protos_dot_controller__pb2
from protos import data_pb2 as protos_dot_data__pb2


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PerformancePacketUpdate = channel.stream_unary(
        '/Controller/PerformancePacketUpdate',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Stop = channel.unary_unary(
        '/Controller/Stop',
        request_serializer=protos_dot_controller__pb2.StopParams.SerializeToString,
        response_deserializer=protos_dot_controller__pb2.StopStatus.FromString,
        )
    self.Liquidate = channel.unary_unary(
        '/Controller/Liquidate',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateLevCap = channel.stream_unary(
        '/Controller/UpdateLevCap',
        request_serializer=protos_dot_controller__pb2.LevCap.SerializeToString,
        response_deserializer=protos_dot_controller__pb2.CapitalAssignmentStatus.FromString,
        )
    self.ClockUpdate = channel.unary_unary(
        '/Controller/ClockUpdate',
        request_serializer=protos_dot_clock__pb2.ClockEvent.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Deploy = channel.stream_unary(
        '/Controller/Deploy',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateGraph = channel.stream_unary(
        '/Controller/UpdateGraph',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PerformancePacketUpdate(self, request_iterator, context):
    """This method is a callback for controllables: each controllable sends back a performance
    packet to the controller by specifying the session_id in the metadata
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Liquidate(self, request, context):
    """orders liquidation of all assets in all the controllables
    we can watch the performance of the strategy in real-time...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLevCap(self, request_iterator, context):
    """rpc Watch (StrategyID) returns (stream Data);

    dynamically updates capital and/or leverage of a running strategy
    NOTE: this information can be obtained from the broker. ex: interactive brokers...
    The controller holds the master account which contains the initial capital of the account...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClockUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Deploy(self, request_iterator, context):
    """TODO: should be able to check for available domains.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateGraph(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PerformancePacketUpdate': grpc.stream_unary_rpc_method_handler(
          servicer.PerformancePacketUpdate,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=protos_dot_controller__pb2.StopParams.FromString,
          response_serializer=protos_dot_controller__pb2.StopStatus.SerializeToString,
      ),
      'Liquidate': grpc.unary_unary_rpc_method_handler(
          servicer.Liquidate,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateLevCap': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateLevCap,
          request_deserializer=protos_dot_controller__pb2.LevCap.FromString,
          response_serializer=protos_dot_controller__pb2.CapitalAssignmentStatus.SerializeToString,
      ),
      'ClockUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ClockUpdate,
          request_deserializer=protos_dot_clock__pb2.ClockEvent.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Deploy': grpc.stream_unary_rpc_method_handler(
          servicer.Deploy,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateGraph': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateGraph,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
