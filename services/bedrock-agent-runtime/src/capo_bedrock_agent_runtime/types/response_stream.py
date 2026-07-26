"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._iter import AnyIterator
from capo_bedrock_agent_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.errors.access_denied_exception
    import capo_bedrock_agent_runtime.errors.bad_gateway_exception
    import capo_bedrock_agent_runtime.errors.conflict_exception
    import capo_bedrock_agent_runtime.errors.dependency_failed_exception
    import capo_bedrock_agent_runtime.errors.internal_server_exception
    import capo_bedrock_agent_runtime.errors.model_not_ready_exception
    import capo_bedrock_agent_runtime.errors.resource_not_found_exception
    import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import capo_bedrock_agent_runtime.errors.throttling_exception
    import capo_bedrock_agent_runtime.errors.validation_exception
    import capo_bedrock_agent_runtime.types.file_part
    import capo_bedrock_agent_runtime.types.payload_part
    import capo_bedrock_agent_runtime.types.return_control_payload
    import capo_bedrock_agent_runtime.types.trace_part


class _ResponseStream_chunk(TypedDict, closed=True):
    chunk: "capo_bedrock_agent_runtime.types.payload_part.PayloadPart"


class _ResponseStream_trace(TypedDict, closed=True):
    trace: "capo_bedrock_agent_runtime.types.trace_part.TracePart"


class _ResponseStream_returnControl(TypedDict, closed=True):
    returnControl: (
        "capo_bedrock_agent_runtime.types.return_control_payload.ReturnControlPayload"
    )


class _ResponseStream_internalServerException(TypedDict, closed=True):
    internalServerException: "capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _ResponseStream_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _ResponseStream_resourceNotFoundException(TypedDict, closed=True):
    resourceNotFoundException: "capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _ResponseStream_serviceQuotaExceededException(TypedDict, closed=True):
    serviceQuotaExceededException: "capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _ResponseStream_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _ResponseStream_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: "capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _ResponseStream_conflictException(TypedDict, closed=True):
    conflictException: (
        "capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _ResponseStream_dependencyFailedException(TypedDict, closed=True):
    dependencyFailedException: "capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _ResponseStream_badGatewayException(TypedDict, closed=True):
    badGatewayException: (
        "capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"
    )


class _ResponseStream_modelNotReadyException(TypedDict, closed=True):
    modelNotReadyException: "capo_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException_"


class _ResponseStream_files(TypedDict, closed=True):
    files: "capo_bedrock_agent_runtime.types.file_part.FilePart"


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
            import capo_bedrock_agent_runtime.types.payload_part

            return capo_bedrock_agent_runtime.types.payload_part.serialize_event_json(
                payload
            )
        case {"trace": payload}:
            import capo_bedrock_agent_runtime.types.trace_part

            return capo_bedrock_agent_runtime.types.trace_part.serialize_event_json(
                payload
            )
        case {"returnControl": payload}:
            import capo_bedrock_agent_runtime.types.return_control_payload

            return capo_bedrock_agent_runtime.types.return_control_payload.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agent_runtime.errors.internal_server_exception

            return capo_bedrock_agent_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_bedrock_agent_runtime.errors.validation_exception

            return capo_bedrock_agent_runtime.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import capo_bedrock_agent_runtime.errors.resource_not_found_exception

            return capo_bedrock_agent_runtime.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception

            return capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_bedrock_agent_runtime.errors.throttling_exception

            return capo_bedrock_agent_runtime.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_bedrock_agent_runtime.errors.access_denied_exception

            return capo_bedrock_agent_runtime.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictException": payload}:
            import capo_bedrock_agent_runtime.errors.conflict_exception

            return capo_bedrock_agent_runtime.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"dependencyFailedException": payload}:
            import capo_bedrock_agent_runtime.errors.dependency_failed_exception

            return capo_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"badGatewayException": payload}:
            import capo_bedrock_agent_runtime.errors.bad_gateway_exception

            return capo_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_event_json(
                payload
            )
        case {"modelNotReadyException": payload}:
            import capo_bedrock_agent_runtime.errors.model_not_ready_exception

            return capo_bedrock_agent_runtime.errors.model_not_ready_exception.serialize_event_json(
                payload
            )
        case {"files": payload}:
            import capo_bedrock_agent_runtime.types.file_part

            return capo_bedrock_agent_runtime.types.file_part.serialize_event_json(
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
                import capo_bedrock_agent_runtime.errors.internal_server_exception

                raise capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException(
                    capo_bedrock_agent_runtime.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import capo_bedrock_agent_runtime.errors.validation_exception

                raise capo_bedrock_agent_runtime.errors.validation_exception.ValidationException(
                    capo_bedrock_agent_runtime.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import capo_bedrock_agent_runtime.errors.resource_not_found_exception

                raise capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException(
                    capo_bedrock_agent_runtime.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceQuotaExceededException":
                import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception

                raise capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import capo_bedrock_agent_runtime.errors.throttling_exception

                raise capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException(
                    capo_bedrock_agent_runtime.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "accessDeniedException":
                import capo_bedrock_agent_runtime.errors.access_denied_exception

                raise capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException(
                    capo_bedrock_agent_runtime.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "conflictException":
                import capo_bedrock_agent_runtime.errors.conflict_exception

                raise capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException(
                    capo_bedrock_agent_runtime.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "dependencyFailedException":
                import capo_bedrock_agent_runtime.errors.dependency_failed_exception

                raise capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException(
                    capo_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_event_json(
                        message
                    )
                )
            case "badGatewayException":
                import capo_bedrock_agent_runtime.errors.bad_gateway_exception

                raise capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException(
                    capo_bedrock_agent_runtime.errors.bad_gateway_exception.deserialize_event_json(
                        message
                    )
                )
            case "modelNotReadyException":
                import capo_bedrock_agent_runtime.errors.model_not_ready_exception

                raise capo_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException(
                    capo_bedrock_agent_runtime.errors.model_not_ready_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"ResponseStream: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "chunk":
            import capo_bedrock_agent_runtime.types.payload_part

            return {
                "chunk": capo_bedrock_agent_runtime.types.payload_part.deserialize_event_json(
                    message
                )
            }
        case "trace":
            import capo_bedrock_agent_runtime.types.trace_part

            return {
                "trace": capo_bedrock_agent_runtime.types.trace_part.deserialize_event_json(
                    message
                )
            }
        case "returnControl":
            import capo_bedrock_agent_runtime.types.return_control_payload

            return {
                "returnControl": capo_bedrock_agent_runtime.types.return_control_payload.deserialize_event_json(
                    message
                )
            }
        case "files":
            import capo_bedrock_agent_runtime.types.file_part

            return {
                "files": capo_bedrock_agent_runtime.types.file_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
