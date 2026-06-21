"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommandStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore._iter import AnyIterator
from aws_sdk_bedrock_agentcore._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.errors.access_denied_exception
    import aws_sdk_bedrock_agentcore.errors.internal_server_exception
    import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
    import aws_sdk_bedrock_agentcore.errors.runtime_client_error
    import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agentcore.errors.throttling_exception
    import aws_sdk_bedrock_agentcore.errors.validation_exception
    import aws_sdk_bedrock_agentcore.types.response_chunk


class _InvokeAgentRuntimeCommandStreamOutput_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_agentcore.types.response_chunk.ResponseChunk"


class _InvokeAgentRuntimeCommandStreamOutput_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException_"


class _InvokeAgentRuntimeCommandStreamOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _InvokeAgentRuntimeCommandStreamOutput_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException_"


class _InvokeAgentRuntimeCommandStreamOutput_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _InvokeAgentRuntimeCommandStreamOutput_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_runtimeClientError(TypedDict):
    runtimeClientError: (
        "aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError_"
    )


_InvokeAgentRuntimeCommandStreamOutput: TypeAlias = (
    _InvokeAgentRuntimeCommandStreamOutput_chunk
    | _InvokeAgentRuntimeCommandStreamOutput_accessDeniedException
    | _InvokeAgentRuntimeCommandStreamOutput_internalServerException
    | _InvokeAgentRuntimeCommandStreamOutput_resourceNotFoundException
    | _InvokeAgentRuntimeCommandStreamOutput_serviceQuotaExceededException
    | _InvokeAgentRuntimeCommandStreamOutput_throttlingException
    | _InvokeAgentRuntimeCommandStreamOutput_validationException
    | _InvokeAgentRuntimeCommandStreamOutput_runtimeClientError
)
InvokeAgentRuntimeCommandStreamOutput: TypeAlias = AnyIterator[
    _InvokeAgentRuntimeCommandStreamOutput
]


def serialize_event_json(value: _InvokeAgentRuntimeCommandStreamOutput) -> bytes:
    match value:
        case {"chunk": payload}:
            import aws_sdk_bedrock_agentcore.types.response_chunk

            return aws_sdk_bedrock_agentcore.types.response_chunk.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import aws_sdk_bedrock_agentcore.errors.access_denied_exception

            return aws_sdk_bedrock_agentcore.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import aws_sdk_bedrock_agentcore.errors.internal_server_exception

            return aws_sdk_bedrock_agentcore.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception

            return aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception

            return aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import aws_sdk_bedrock_agentcore.errors.throttling_exception

            return aws_sdk_bedrock_agentcore.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import aws_sdk_bedrock_agentcore.errors.validation_exception

            return aws_sdk_bedrock_agentcore.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"runtimeClientError": payload}:
            import aws_sdk_bedrock_agentcore.errors.runtime_client_error

            return aws_sdk_bedrock_agentcore.errors.runtime_client_error.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeAgentRuntimeCommandStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _InvokeAgentRuntimeCommandStreamOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "accessDeniedException":
                import aws_sdk_bedrock_agentcore.errors.access_denied_exception

                raise aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException(
                    aws_sdk_bedrock_agentcore.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "internalServerException":
                import aws_sdk_bedrock_agentcore.errors.internal_server_exception

                raise aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException(
                    aws_sdk_bedrock_agentcore.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception

                raise aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException(
                    aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceQuotaExceededException":
                import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception

                raise aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import aws_sdk_bedrock_agentcore.errors.throttling_exception

                raise aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException(
                    aws_sdk_bedrock_agentcore.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import aws_sdk_bedrock_agentcore.errors.validation_exception

                raise aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException(
                    aws_sdk_bedrock_agentcore.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "runtimeClientError":
                import aws_sdk_bedrock_agentcore.errors.runtime_client_error

                raise aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError(
                    aws_sdk_bedrock_agentcore.errors.runtime_client_error.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"InvokeAgentRuntimeCommandStreamOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "chunk":
            import aws_sdk_bedrock_agentcore.types.response_chunk

            return {
                "chunk": aws_sdk_bedrock_agentcore.types.response_chunk.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeAgentRuntimeCommandStreamOutput: unrecognized event-type {event_type!r}"
            )
