"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime._iter import AnyIterator
from aws_sdk_bedrock_agent_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
    import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
    import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
    import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
    import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
    import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
    import aws_sdk_bedrock_agent_runtime.errors.validation_exception
    import aws_sdk_bedrock_agent_runtime.types.flow_completion_event
    import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event
    import aws_sdk_bedrock_agent_runtime.types.flow_output_event
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_event


class _FlowResponseStream_flowOutputEvent(TypedDict):
    flowOutputEvent: (
        "aws_sdk_bedrock_agent_runtime.types.flow_output_event.FlowOutputEvent"
    )


class _FlowResponseStream_flowCompletionEvent(TypedDict):
    flowCompletionEvent: (
        "aws_sdk_bedrock_agent_runtime.types.flow_completion_event.FlowCompletionEvent"
    )


class _FlowResponseStream_flowTraceEvent(TypedDict):
    flowTraceEvent: (
        "aws_sdk_bedrock_agent_runtime.types.flow_trace_event.FlowTraceEvent"
    )


class _FlowResponseStream_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _FlowResponseStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _FlowResponseStream_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _FlowResponseStream_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _FlowResponseStream_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _FlowResponseStream_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _FlowResponseStream_conflictException(TypedDict):
    conflictException: (
        "aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _FlowResponseStream_dependencyFailedException(TypedDict):
    dependencyFailedException: "aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _FlowResponseStream_badGatewayException(TypedDict):
    badGatewayException: "aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"


class _FlowResponseStream_flowMultiTurnInputRequestEvent(TypedDict):
    flowMultiTurnInputRequestEvent: "aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.FlowMultiTurnInputRequestEvent"


_FlowResponseStream: TypeAlias = (
    _FlowResponseStream_flowOutputEvent
    | _FlowResponseStream_flowCompletionEvent
    | _FlowResponseStream_flowTraceEvent
    | _FlowResponseStream_internalServerException
    | _FlowResponseStream_validationException
    | _FlowResponseStream_resourceNotFoundException
    | _FlowResponseStream_serviceQuotaExceededException
    | _FlowResponseStream_throttlingException
    | _FlowResponseStream_accessDeniedException
    | _FlowResponseStream_conflictException
    | _FlowResponseStream_dependencyFailedException
    | _FlowResponseStream_badGatewayException
    | _FlowResponseStream_flowMultiTurnInputRequestEvent
)
FlowResponseStream: TypeAlias = AnyIterator[_FlowResponseStream]


def serialize_event_json(value: _FlowResponseStream) -> bytes:
    match value:
        case {"flowOutputEvent": payload}:
            import aws_sdk_bedrock_agent_runtime.types.flow_output_event

            return aws_sdk_bedrock_agent_runtime.types.flow_output_event.serialize_event_json(
                payload
            )
        case {"flowCompletionEvent": payload}:
            import aws_sdk_bedrock_agent_runtime.types.flow_completion_event

            return aws_sdk_bedrock_agent_runtime.types.flow_completion_event.serialize_event_json(
                payload
            )
        case {"flowTraceEvent": payload}:
            import aws_sdk_bedrock_agent_runtime.types.flow_trace_event

            return aws_sdk_bedrock_agent_runtime.types.flow_trace_event.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception

            return aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.validation_exception

            return aws_sdk_bedrock_agent_runtime.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception

            return aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception

            return aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.throttling_exception

            return aws_sdk_bedrock_agent_runtime.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception

            return aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.conflict_exception

            return aws_sdk_bedrock_agent_runtime.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"dependencyFailedException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception

            return aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"badGatewayException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception

            return aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_event_json(
                payload
            )
        case {"flowMultiTurnInputRequestEvent": payload}:
            import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event

            return aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"FlowResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _FlowResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "internalServerException":
                import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception

                raise aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException(
                    aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import aws_sdk_bedrock_agent_runtime.errors.validation_exception

                raise aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException(
                    aws_sdk_bedrock_agent_runtime.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception

                raise aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException(
                    aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceQuotaExceededException":
                import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception

                raise aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import aws_sdk_bedrock_agent_runtime.errors.throttling_exception

                raise aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException(
                    aws_sdk_bedrock_agent_runtime.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "accessDeniedException":
                import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception

                raise aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException(
                    aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "conflictException":
                import aws_sdk_bedrock_agent_runtime.errors.conflict_exception

                raise aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException(
                    aws_sdk_bedrock_agent_runtime.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "dependencyFailedException":
                import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception

                raise aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException(
                    aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_event_json(
                        message
                    )
                )
            case "badGatewayException":
                import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception

                raise aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException(
                    aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"FlowResponseStream: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "flowOutputEvent":
            import aws_sdk_bedrock_agent_runtime.types.flow_output_event

            return {
                "flowOutputEvent": aws_sdk_bedrock_agent_runtime.types.flow_output_event.deserialize_event_json(
                    message
                )
            }
        case "flowCompletionEvent":
            import aws_sdk_bedrock_agent_runtime.types.flow_completion_event

            return {
                "flowCompletionEvent": aws_sdk_bedrock_agent_runtime.types.flow_completion_event.deserialize_event_json(
                    message
                )
            }
        case "flowTraceEvent":
            import aws_sdk_bedrock_agent_runtime.types.flow_trace_event

            return {
                "flowTraceEvent": aws_sdk_bedrock_agent_runtime.types.flow_trace_event.deserialize_event_json(
                    message
                )
            }
        case "flowMultiTurnInputRequestEvent":
            import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event

            return {
                "flowMultiTurnInputRequestEvent": aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"FlowResponseStream: unrecognized event-type {event_type!r}"
            )
