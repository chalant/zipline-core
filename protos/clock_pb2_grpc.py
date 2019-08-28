# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import clock_pb2 as protos_dot_clock__pb2


class SimulationClockRouterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.unary_unary(
        '/SimulationClockRouter/Register',
        request_serializer=protos_dot_clock__pb2.SimulationClockParameters.SerializeToString,
        response_deserializer=protos_dot_clock__pb2.Attributes.FromString,
        )
    self.Run = channel.unary_unary(
        '/SimulationClockRouter/Run',
        request_serializer=protos_dot_clock__pb2.SimulationRunParameters.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class SimulationClockRouterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimulationClockRouterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=protos_dot_clock__pb2.SimulationClockParameters.FromString,
          response_serializer=protos_dot_clock__pb2.Attributes.SerializeToString,
      ),
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=protos_dot_clock__pb2.SimulationRunParameters.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SimulationClockRouter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class RealtimeClockRouterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.unary_unary(
        '/RealtimeClockRouter/Register',
        request_serializer=protos_dot_clock__pb2.RealtimeClockParameters.SerializeToString,
        response_deserializer=protos_dot_clock__pb2.Attributes.FromString,
        )


class RealtimeClockRouterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RealtimeClockRouterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=protos_dot_clock__pb2.RealtimeClockParameters.FromString,
          response_serializer=protos_dot_clock__pb2.Attributes.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RealtimeClockRouter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class RealtimeClockStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.unary_unary(
        '/RealtimeClock/Register',
        request_serializer=protos_dot_clock__pb2.RealtimeClockParameters.SerializeToString,
        response_deserializer=protos_dot_clock__pb2.Attributes.FromString,
        )
    self.Run = channel.unary_unary(
        '/RealtimeClock/Run',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class RealtimeClockServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RealtimeClockServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=protos_dot_clock__pb2.RealtimeClockParameters.FromString,
          response_serializer=protos_dot_clock__pb2.Attributes.SerializeToString,
      ),
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RealtimeClock', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SimulationClockStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.unary_unary(
        '/SimulationClock/Register',
        request_serializer=protos_dot_clock__pb2.SimulationClockParameters.SerializeToString,
        response_deserializer=protos_dot_clock__pb2.Attributes.FromString,
        )
    self.Run = channel.unary_unary(
        '/SimulationClock/Run',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetState = channel.unary_unary(
        '/SimulationClock/GetState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=protos_dot_clock__pb2.State.FromString,
        )


class SimulationClockServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimulationClockServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=protos_dot_clock__pb2.SimulationClockParameters.FromString,
          response_serializer=protos_dot_clock__pb2.Attributes.SerializeToString,
      ),
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=protos_dot_clock__pb2.State.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SimulationClock', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ClockListenerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.OnClockEvent = channel.unary_unary(
        '/ClockListener/OnClockEvent',
        request_serializer=protos_dot_clock__pb2.ClockEvent.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ClockListenerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def OnClockEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClockListenerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'OnClockEvent': grpc.unary_unary_rpc_method_handler(
          servicer.OnClockEvent,
          request_deserializer=protos_dot_clock__pb2.ClockEvent.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ClockListener', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
