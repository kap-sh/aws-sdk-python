"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime._iter import AnyIterator
from aws_sdk_bedrock_agent_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
    import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
    import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
    import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
    import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception
    import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
    import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
    import aws_sdk_bedrock_agent_runtime.errors.validation_exception
    import aws_sdk_bedrock_agent_runtime.types.file_part
    import aws_sdk_bedrock_agent_runtime.types.payload_part
    import aws_sdk_bedrock_agent_runtime.types.return_control_payload
    import aws_sdk_bedrock_agent_runtime.types.trace_part


class _ResponseStream_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_agent_runtime.types.payload_part.PayloadPart"


class _ResponseStream_trace(TypedDict):
    trace: "aws_sdk_bedrock_agent_runtime.types.trace_part.TracePart"


class _ResponseStream_returnControl(TypedDict):
    returnControl: "aws_sdk_bedrock_agent_runtime.types.return_control_payload.ReturnControlPayload"


class _ResponseStream_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _ResponseStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _ResponseStream_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _ResponseStream_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _ResponseStream_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _ResponseStream_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _ResponseStream_conflictException(TypedDict):
    conflictException: (
        "aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _ResponseStream_dependencyFailedException(TypedDict):
    dependencyFailedException: "aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _ResponseStream_badGatewayException(TypedDict):
    badGatewayException: "aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"


class _ResponseStream_modelNotReadyException(TypedDict):
    modelNotReadyException: "aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException_"


class _ResponseStream_files(TypedDict):
    files: "aws_sdk_bedrock_agent_runtime.types.file_part.FilePart"


_ResponseStream: TypeAlias = (
    _ResponseStream_chunk
    | _ResponseStream_trace
    | _ResponseStream_returnControl
    | _ResponseStream_internalServerException
    | _ResponseStream_validationException
    | _ResponseStream_resourceNotFoundException
    | _ResponseStream_serviceQuotaExceededException
    | _ResponseStream_throttlingException
    | _ResponseStream_accessDeniedException
    | _ResponseStream_conflictException
    | _ResponseStream_dependencyFailedException
    | _ResponseStream_badGatewayException
    | _ResponseStream_modelNotReadyException
    | _ResponseStream_files
)
ResponseStream: TypeAlias = AnyIterator[_ResponseStream]


def serialize_event_json(value: _ResponseStream) -> bytes:
    match value:
        case {"chunk": payload}:
            import aws_sdk_bedrock_agent_runtime.types.payload_part

            return (
                aws_sdk_bedrock_agent_runtime.types.payload_part.serialize_event_json(
                    payload
                )
            )
        case {"trace": payload}:
            import aws_sdk_bedrock_agent_runtime.types.trace_part

            return aws_sdk_bedrock_agent_runtime.types.trace_part.serialize_event_json(
                payload
            )
        case {"returnControl": payload}:
            import aws_sdk_bedrock_agent_runtime.types.return_control_payload

            return aws_sdk_bedrock_agent_runtime.types.return_control_payload.serialize_event_json(
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
        case {"modelNotReadyException": payload}:
            import aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception

            return aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception.serialize_event_json(
                payload
            )
        case {"files": payload}:
            import aws_sdk_bedrock_agent_runtime.types.file_part

            return aws_sdk_bedrock_agent_runtime.types.file_part.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ResponseStream:
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
            case "modelNotReadyException":
                import aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception

                raise aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException(
                    aws_sdk_bedrock_agent_runtime.errors.model_not_ready_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"ResponseStream: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "chunk":
            import aws_sdk_bedrock_agent_runtime.types.payload_part

            return {
                "chunk": aws_sdk_bedrock_agent_runtime.types.payload_part.deserialize_event_json(
                    message
                )
            }
        case "trace":
            import aws_sdk_bedrock_agent_runtime.types.trace_part

            return {
                "trace": aws_sdk_bedrock_agent_runtime.types.trace_part.deserialize_event_json(
                    message
                )
            }
        case "returnControl":
            import aws_sdk_bedrock_agent_runtime.types.return_control_payload

            return {
                "returnControl": aws_sdk_bedrock_agent_runtime.types.return_control_payload.deserialize_event_json(
                    message
                )
            }
        case "files":
            import aws_sdk_bedrock_agent_runtime.types.file_part

            return {
                "files": aws_sdk_bedrock_agent_runtime.types.file_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
