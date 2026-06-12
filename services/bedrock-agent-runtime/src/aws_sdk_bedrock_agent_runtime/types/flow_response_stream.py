"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
    import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
    import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
    import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
    import aws_sdk_bedrock_agent_runtime.types.flow_output_event
    import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
    import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
    import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_event
    import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_agent_runtime.errors.validation_exception
    import aws_sdk_bedrock_agent_runtime.types.flow_completion_event

class _FlowResponseStream_flowOutputEvent(TypedDict):
    flowOutputEvent: "aws_sdk_bedrock_agent_runtime.types.flow_output_event.FlowOutputEvent"


class _FlowResponseStream_flowCompletionEvent(TypedDict):
    flowCompletionEvent: "aws_sdk_bedrock_agent_runtime.types.flow_completion_event.FlowCompletionEvent"


class _FlowResponseStream_flowTraceEvent(TypedDict):
    flowTraceEvent: "aws_sdk_bedrock_agent_runtime.types.flow_trace_event.FlowTraceEvent"


class _FlowResponseStream_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException"


class _FlowResponseStream_validationException(TypedDict):
    validationException: "aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException"


class _FlowResponseStream_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException"


class _FlowResponseStream_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException"


class _FlowResponseStream_throttlingException(TypedDict):
    throttlingException: "aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException"


class _FlowResponseStream_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException"


class _FlowResponseStream_conflictException(TypedDict):
    conflictException: "aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException"


class _FlowResponseStream_dependencyFailedException(TypedDict):
    dependencyFailedException: "aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException"


class _FlowResponseStream_badGatewayException(TypedDict):
    badGatewayException: "aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException"


class _FlowResponseStream_flowMultiTurnInputRequestEvent(TypedDict):
    flowMultiTurnInputRequestEvent: "aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.FlowMultiTurnInputRequestEvent"

FlowResponseStream: TypeAlias = _FlowResponseStream_flowOutputEvent | _FlowResponseStream_flowCompletionEvent | _FlowResponseStream_flowTraceEvent | _FlowResponseStream_internalServerException | _FlowResponseStream_validationException | _FlowResponseStream_resourceNotFoundException | _FlowResponseStream_serviceQuotaExceededException | _FlowResponseStream_throttlingException | _FlowResponseStream_accessDeniedException | _FlowResponseStream_conflictException | _FlowResponseStream_dependencyFailedException | _FlowResponseStream_badGatewayException | _FlowResponseStream_flowMultiTurnInputRequestEvent

# --- restJson1 ser/de ---
def serialize_json(value: FlowResponseStream) -> dict:
    if "flowOutputEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_output_event
        return {"flowOutputEvent": aws_sdk_bedrock_agent_runtime.types.flow_output_event.serialize_json(value["flowOutputEvent"])}
    elif "flowCompletionEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_completion_event
        return {"flowCompletionEvent": aws_sdk_bedrock_agent_runtime.types.flow_completion_event.serialize_json(value["flowCompletionEvent"])}
    elif "flowTraceEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_event
        return {"flowTraceEvent": aws_sdk_bedrock_agent_runtime.types.flow_trace_event.serialize_json(value["flowTraceEvent"])}
    elif "internalServerException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
        return {"internalServerException": aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.serialize_json(value["internalServerException"])}
    elif "validationException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.validation_exception
        return {"validationException": aws_sdk_bedrock_agent_runtime.errors.validation_exception.serialize_json(value["validationException"])}
    elif "resourceNotFoundException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
        return {"resourceNotFoundException": aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.serialize_json(value["resourceNotFoundException"])}
    elif "serviceQuotaExceededException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
        return {"serviceQuotaExceededException": aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.serialize_json(value["serviceQuotaExceededException"])}
    elif "throttlingException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
        return {"throttlingException": aws_sdk_bedrock_agent_runtime.errors.throttling_exception.serialize_json(value["throttlingException"])}
    elif "accessDeniedException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
        return {"accessDeniedException": aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.serialize_json(value["accessDeniedException"])}
    elif "conflictException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
        return {"conflictException": aws_sdk_bedrock_agent_runtime.errors.conflict_exception.serialize_json(value["conflictException"])}
    elif "dependencyFailedException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
        return {"dependencyFailedException": aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_json(value["dependencyFailedException"])}
    elif "badGatewayException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
        return {"badGatewayException": aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_json(value["badGatewayException"])}
    elif "flowMultiTurnInputRequestEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event
        return {"flowMultiTurnInputRequestEvent": aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.serialize_json(value["flowMultiTurnInputRequestEvent"])}
    else:
        raise SerializationError("FlowResponseStream: no variant present")


def deserialize_json(data: dict) -> FlowResponseStream:
    if "flowOutputEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_output_event
        return {"flowOutputEvent": aws_sdk_bedrock_agent_runtime.types.flow_output_event.deserialize_json(data["flowOutputEvent"])}
    elif "flowCompletionEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_completion_event
        return {"flowCompletionEvent": aws_sdk_bedrock_agent_runtime.types.flow_completion_event.deserialize_json(data["flowCompletionEvent"])}
    elif "flowTraceEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_event
        return {"flowTraceEvent": aws_sdk_bedrock_agent_runtime.types.flow_trace_event.deserialize_json(data["flowTraceEvent"])}
    elif "internalServerException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
        return {"internalServerException": aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.deserialize_json(data["internalServerException"])}
    elif "validationException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.validation_exception
        return {"validationException": aws_sdk_bedrock_agent_runtime.errors.validation_exception.deserialize_json(data["validationException"])}
    elif "resourceNotFoundException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
        return {"resourceNotFoundException": aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.deserialize_json(data["resourceNotFoundException"])}
    elif "serviceQuotaExceededException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
        return {"serviceQuotaExceededException": aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.deserialize_json(data["serviceQuotaExceededException"])}
    elif "throttlingException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
        return {"throttlingException": aws_sdk_bedrock_agent_runtime.errors.throttling_exception.deserialize_json(data["throttlingException"])}
    elif "accessDeniedException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
        return {"accessDeniedException": aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.deserialize_json(data["accessDeniedException"])}
    elif "conflictException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
        return {"conflictException": aws_sdk_bedrock_agent_runtime.errors.conflict_exception.deserialize_json(data["conflictException"])}
    elif "dependencyFailedException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
        return {"dependencyFailedException": aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_json(data["dependencyFailedException"])}
    elif "badGatewayException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
        return {"badGatewayException": aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.deserialize_json(data["badGatewayException"])}
    elif "flowMultiTurnInputRequestEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event
        return {"flowMultiTurnInputRequestEvent": aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.deserialize_json(data["flowMultiTurnInputRequestEvent"])}
    else:
        raise DeserializationError("FlowResponseStream: no recognized variant key")