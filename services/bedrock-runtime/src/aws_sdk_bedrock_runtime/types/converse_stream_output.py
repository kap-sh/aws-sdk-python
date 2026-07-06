"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime._iter import AnyIterator
from aws_sdk_bedrock_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_runtime.errors.model_stream_error_exception
    import aws_sdk_bedrock_runtime.errors.service_unavailable_exception
    import aws_sdk_bedrock_runtime.errors.throttling_exception
    import aws_sdk_bedrock_runtime.errors.validation_exception
    import aws_sdk_bedrock_runtime.types.content_block_delta_event
    import aws_sdk_bedrock_runtime.types.content_block_start_event
    import aws_sdk_bedrock_runtime.types.content_block_stop_event
    import aws_sdk_bedrock_runtime.types.converse_stream_metadata_event
    import aws_sdk_bedrock_runtime.types.message_start_event
    import aws_sdk_bedrock_runtime.types.message_stop_event


class _ConverseStreamOutput_messageStart(TypedDict, closed=True):
    messageStart: "aws_sdk_bedrock_runtime.types.message_start_event.MessageStartEvent"


class _ConverseStreamOutput_contentBlockStart(TypedDict, closed=True):
    contentBlockStart: (
        "aws_sdk_bedrock_runtime.types.content_block_start_event.ContentBlockStartEvent"
    )


class _ConverseStreamOutput_contentBlockDelta(TypedDict, closed=True):
    contentBlockDelta: (
        "aws_sdk_bedrock_runtime.types.content_block_delta_event.ContentBlockDeltaEvent"
    )


class _ConverseStreamOutput_contentBlockStop(TypedDict, closed=True):
    contentBlockStop: (
        "aws_sdk_bedrock_runtime.types.content_block_stop_event.ContentBlockStopEvent"
    )


class _ConverseStreamOutput_messageStop(TypedDict, closed=True):
    messageStop: "aws_sdk_bedrock_runtime.types.message_stop_event.MessageStopEvent"


class _ConverseStreamOutput_metadata(TypedDict, closed=True):
    metadata: "aws_sdk_bedrock_runtime.types.converse_stream_metadata_event.ConverseStreamMetadataEvent"


class _ConverseStreamOutput_internalServerException(TypedDict, closed=True):
    internalServerException: "aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException_"


class _ConverseStreamOutput_modelStreamErrorException(TypedDict, closed=True):
    modelStreamErrorException: "aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _ConverseStreamOutput_validationException(TypedDict, closed=True):
    validationException: (
        "aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _ConverseStreamOutput_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _ConverseStreamOutput_serviceUnavailableException(TypedDict, closed=True):
    serviceUnavailableException: "aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


_ConverseStreamOutput: TypeAlias = (
    _ConverseStreamOutput_messageStart
    | _ConverseStreamOutput_contentBlockStart
    | _ConverseStreamOutput_contentBlockDelta
    | _ConverseStreamOutput_contentBlockStop
    | _ConverseStreamOutput_messageStop
    | _ConverseStreamOutput_metadata
    | _ConverseStreamOutput_internalServerException
    | _ConverseStreamOutput_modelStreamErrorException
    | _ConverseStreamOutput_validationException
    | _ConverseStreamOutput_throttlingException
    | _ConverseStreamOutput_serviceUnavailableException
)
ConverseStreamOutput: TypeAlias = AnyIterator[_ConverseStreamOutput]


def serialize_event_json(value: _ConverseStreamOutput) -> bytes:
    match value:
        case {"messageStart": payload}:
            import aws_sdk_bedrock_runtime.types.message_start_event

            return (
                aws_sdk_bedrock_runtime.types.message_start_event.serialize_event_json(
                    payload
                )
            )
        case {"contentBlockStart": payload}:
            import aws_sdk_bedrock_runtime.types.content_block_start_event

            return aws_sdk_bedrock_runtime.types.content_block_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockDelta": payload}:
            import aws_sdk_bedrock_runtime.types.content_block_delta_event

            return aws_sdk_bedrock_runtime.types.content_block_delta_event.serialize_event_json(
                payload
            )
        case {"contentBlockStop": payload}:
            import aws_sdk_bedrock_runtime.types.content_block_stop_event

            return aws_sdk_bedrock_runtime.types.content_block_stop_event.serialize_event_json(
                payload
            )
        case {"messageStop": payload}:
            import aws_sdk_bedrock_runtime.types.message_stop_event

            return (
                aws_sdk_bedrock_runtime.types.message_stop_event.serialize_event_json(
                    payload
                )
            )
        case {"metadata": payload}:
            import aws_sdk_bedrock_runtime.types.converse_stream_metadata_event

            return aws_sdk_bedrock_runtime.types.converse_stream_metadata_event.serialize_event_json(
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
        case {"serviceUnavailableException": payload}:
            import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

            return aws_sdk_bedrock_runtime.errors.service_unavailable_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ConverseStreamOutput: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ConverseStreamOutput:
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
            case "serviceUnavailableException":
                import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

                raise aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException(
                    aws_sdk_bedrock_runtime.errors.service_unavailable_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"ConverseStreamOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "messageStart":
            import aws_sdk_bedrock_runtime.types.message_start_event

            return {
                "messageStart": aws_sdk_bedrock_runtime.types.message_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStart":
            import aws_sdk_bedrock_runtime.types.content_block_start_event

            return {
                "contentBlockStart": aws_sdk_bedrock_runtime.types.content_block_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockDelta":
            import aws_sdk_bedrock_runtime.types.content_block_delta_event

            return {
                "contentBlockDelta": aws_sdk_bedrock_runtime.types.content_block_delta_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStop":
            import aws_sdk_bedrock_runtime.types.content_block_stop_event

            return {
                "contentBlockStop": aws_sdk_bedrock_runtime.types.content_block_stop_event.deserialize_event_json(
                    message
                )
            }
        case "messageStop":
            import aws_sdk_bedrock_runtime.types.message_stop_event

            return {
                "messageStop": aws_sdk_bedrock_runtime.types.message_stop_event.deserialize_event_json(
                    message
                )
            }
        case "metadata":
            import aws_sdk_bedrock_runtime.types.converse_stream_metadata_event

            return {
                "metadata": aws_sdk_bedrock_runtime.types.converse_stream_metadata_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"ConverseStreamOutput: unrecognized event-type {event_type!r}"
            )
