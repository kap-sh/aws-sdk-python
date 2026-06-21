"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime._iter import AnyIterator
from aws_sdk_bedrock_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_runtime.errors.model_stream_error_exception
    import aws_sdk_bedrock_runtime.errors.model_timeout_exception
    import aws_sdk_bedrock_runtime.errors.service_unavailable_exception
    import aws_sdk_bedrock_runtime.errors.throttling_exception
    import aws_sdk_bedrock_runtime.errors.validation_exception
    import aws_sdk_bedrock_runtime.types.payload_part


class _ResponseStream_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_runtime.types.payload_part.PayloadPart"


class _ResponseStream_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException_"


class _ResponseStream_modelStreamErrorException(TypedDict):
    modelStreamErrorException: "aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _ResponseStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _ResponseStream_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _ResponseStream_modelTimeoutException(TypedDict):
    modelTimeoutException: (
        "aws_sdk_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException_"
    )


class _ResponseStream_serviceUnavailableException(TypedDict):
    serviceUnavailableException: "aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


_ResponseStream: TypeAlias = (
    _ResponseStream_chunk
    | _ResponseStream_internalServerException
    | _ResponseStream_modelStreamErrorException
    | _ResponseStream_validationException
    | _ResponseStream_throttlingException
    | _ResponseStream_modelTimeoutException
    | _ResponseStream_serviceUnavailableException
)
ResponseStream: TypeAlias = AnyIterator[_ResponseStream]


def serialize_event_json(value: _ResponseStream) -> bytes:
    match value:
        case {"chunk": payload}:
            import aws_sdk_bedrock_runtime.types.payload_part

            return aws_sdk_bedrock_runtime.types.payload_part.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import aws_sdk_bedrock_runtime.errors.internal_server_exception

            return aws_sdk_bedrock_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"modelStreamErrorException": payload}:
            import aws_sdk_bedrock_runtime.errors.model_stream_error_exception

            return aws_sdk_bedrock_runtime.errors.model_stream_error_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import aws_sdk_bedrock_runtime.errors.validation_exception

            return aws_sdk_bedrock_runtime.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import aws_sdk_bedrock_runtime.errors.throttling_exception

            return aws_sdk_bedrock_runtime.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"modelTimeoutException": payload}:
            import aws_sdk_bedrock_runtime.errors.model_timeout_exception

            return aws_sdk_bedrock_runtime.errors.model_timeout_exception.serialize_event_json(
                payload
            )
        case {"serviceUnavailableException": payload}:
            import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

            return aws_sdk_bedrock_runtime.errors.service_unavailable_exception.serialize_event_json(
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
                import aws_sdk_bedrock_runtime.errors.internal_server_exception

                raise aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException(
                    aws_sdk_bedrock_runtime.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "modelStreamErrorException":
                import aws_sdk_bedrock_runtime.errors.model_stream_error_exception

                raise aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException(
                    aws_sdk_bedrock_runtime.errors.model_stream_error_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import aws_sdk_bedrock_runtime.errors.validation_exception

                raise aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException(
                    aws_sdk_bedrock_runtime.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import aws_sdk_bedrock_runtime.errors.throttling_exception

                raise aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException(
                    aws_sdk_bedrock_runtime.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "modelTimeoutException":
                import aws_sdk_bedrock_runtime.errors.model_timeout_exception

                raise aws_sdk_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException(
                    aws_sdk_bedrock_runtime.errors.model_timeout_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceUnavailableException":
                import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

                raise aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException(
                    aws_sdk_bedrock_runtime.errors.service_unavailable_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"ResponseStream: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "chunk":
            import aws_sdk_bedrock_runtime.types.payload_part

            return {
                "chunk": aws_sdk_bedrock_runtime.types.payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
