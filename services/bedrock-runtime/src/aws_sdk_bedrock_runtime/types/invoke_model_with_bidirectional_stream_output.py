"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime._iter import AnyIterator
from aws_sdk_bedrock_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_runtime.errors.model_stream_error_exception
    import aws_sdk_bedrock_runtime.errors.model_timeout_exception
    import aws_sdk_bedrock_runtime.errors.service_unavailable_exception
    import aws_sdk_bedrock_runtime.errors.throttling_exception
    import aws_sdk_bedrock_runtime.errors.validation_exception
    import aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part


class _InvokeModelWithBidirectionalStreamOutput_chunk(TypedDict, closed=True):
    chunk: "aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part.BidirectionalOutputPayloadPart"


class _InvokeModelWithBidirectionalStreamOutput_internalServerException(
    TypedDict, closed=True
):
    internalServerException: "aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException_"


class _InvokeModelWithBidirectionalStreamOutput_modelStreamErrorException(
    TypedDict, closed=True
):
    modelStreamErrorException: "aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _InvokeModelWithBidirectionalStreamOutput_validationException(
    TypedDict, closed=True
):
    validationException: (
        "aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_throttlingException(
    TypedDict, closed=True
):
    throttlingException: (
        "aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_modelTimeoutException(
    TypedDict, closed=True
):
    modelTimeoutException: (
        "aws_sdk_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_serviceUnavailableException(
    TypedDict, closed=True
):
    serviceUnavailableException: "aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


_InvokeModelWithBidirectionalStreamOutput: TypeAlias = (
    _InvokeModelWithBidirectionalStreamOutput_chunk
    | _InvokeModelWithBidirectionalStreamOutput_internalServerException
    | _InvokeModelWithBidirectionalStreamOutput_modelStreamErrorException
    | _InvokeModelWithBidirectionalStreamOutput_validationException
    | _InvokeModelWithBidirectionalStreamOutput_throttlingException
    | _InvokeModelWithBidirectionalStreamOutput_modelTimeoutException
    | _InvokeModelWithBidirectionalStreamOutput_serviceUnavailableException
)
InvokeModelWithBidirectionalStreamOutput: TypeAlias = AnyIterator[
    _InvokeModelWithBidirectionalStreamOutput
]


def serialize_event_json(value: _InvokeModelWithBidirectionalStreamOutput) -> bytes:
    match value:
        case {"chunk": payload}:
            import aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part

            return aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part.serialize_event_json(
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
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message,
) -> _InvokeModelWithBidirectionalStreamOutput:
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
        raise ValueError(
            f"InvokeModelWithBidirectionalStreamOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "chunk":
            import aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part

            return {
                "chunk": aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamOutput: unrecognized event-type {event_type!r}"
            )
