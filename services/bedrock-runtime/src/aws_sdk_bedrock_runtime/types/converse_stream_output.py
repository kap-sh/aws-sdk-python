"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

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


class _ConverseStreamOutput_messageStart(TypedDict):
    messageStart: "aws_sdk_bedrock_runtime.types.message_start_event.MessageStartEvent"


class _ConverseStreamOutput_contentBlockStart(TypedDict):
    contentBlockStart: (
        "aws_sdk_bedrock_runtime.types.content_block_start_event.ContentBlockStartEvent"
    )


class _ConverseStreamOutput_contentBlockDelta(TypedDict):
    contentBlockDelta: (
        "aws_sdk_bedrock_runtime.types.content_block_delta_event.ContentBlockDeltaEvent"
    )


class _ConverseStreamOutput_contentBlockStop(TypedDict):
    contentBlockStop: (
        "aws_sdk_bedrock_runtime.types.content_block_stop_event.ContentBlockStopEvent"
    )


class _ConverseStreamOutput_messageStop(TypedDict):
    messageStop: "aws_sdk_bedrock_runtime.types.message_stop_event.MessageStopEvent"


class _ConverseStreamOutput_metadata(TypedDict):
    metadata: "aws_sdk_bedrock_runtime.types.converse_stream_metadata_event.ConverseStreamMetadataEvent"


class _ConverseStreamOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException_"


class _ConverseStreamOutput_modelStreamErrorException(TypedDict):
    modelStreamErrorException: "aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _ConverseStreamOutput_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _ConverseStreamOutput_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _ConverseStreamOutput_serviceUnavailableException(TypedDict):
    serviceUnavailableException: "aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


ConverseStreamOutput: TypeAlias = (
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


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamOutput) -> dict:
    if "messageStart" in value:
        import aws_sdk_bedrock_runtime.types.message_start_event

        return {
            "messageStart": aws_sdk_bedrock_runtime.types.message_start_event.serialize_json(
                value["messageStart"]
            )
        }
    elif "contentBlockStart" in value:
        import aws_sdk_bedrock_runtime.types.content_block_start_event

        return {
            "contentBlockStart": aws_sdk_bedrock_runtime.types.content_block_start_event.serialize_json(
                value["contentBlockStart"]
            )
        }
    elif "contentBlockDelta" in value:
        import aws_sdk_bedrock_runtime.types.content_block_delta_event

        return {
            "contentBlockDelta": aws_sdk_bedrock_runtime.types.content_block_delta_event.serialize_json(
                value["contentBlockDelta"]
            )
        }
    elif "contentBlockStop" in value:
        import aws_sdk_bedrock_runtime.types.content_block_stop_event

        return {
            "contentBlockStop": aws_sdk_bedrock_runtime.types.content_block_stop_event.serialize_json(
                value["contentBlockStop"]
            )
        }
    elif "messageStop" in value:
        import aws_sdk_bedrock_runtime.types.message_stop_event

        return {
            "messageStop": aws_sdk_bedrock_runtime.types.message_stop_event.serialize_json(
                value["messageStop"]
            )
        }
    elif "metadata" in value:
        import aws_sdk_bedrock_runtime.types.converse_stream_metadata_event

        return {
            "metadata": aws_sdk_bedrock_runtime.types.converse_stream_metadata_event.serialize_json(
                value["metadata"]
            )
        }
    elif "internalServerException" in value:
        import aws_sdk_bedrock_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_runtime.errors.internal_server_exception.serialize_json(
                value["internalServerException"]
            )
        }
    elif "modelStreamErrorException" in value:
        import aws_sdk_bedrock_runtime.errors.model_stream_error_exception

        return {
            "modelStreamErrorException": aws_sdk_bedrock_runtime.errors.model_stream_error_exception.serialize_json(
                value["modelStreamErrorException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_bedrock_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_runtime.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    elif "throttlingException" in value:
        import aws_sdk_bedrock_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_runtime.errors.throttling_exception.serialize_json(
                value["throttlingException"]
            )
        }
    elif "serviceUnavailableException" in value:
        import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

        return {
            "serviceUnavailableException": aws_sdk_bedrock_runtime.errors.service_unavailable_exception.serialize_json(
                value["serviceUnavailableException"]
            )
        }
    else:
        raise SerializationError("ConverseStreamOutput: no variant present")


def deserialize_json(data: dict) -> ConverseStreamOutput:
    if "messageStart" in data:
        import aws_sdk_bedrock_runtime.types.message_start_event

        return {
            "messageStart": aws_sdk_bedrock_runtime.types.message_start_event.deserialize_json(
                data["messageStart"]
            )
        }
    elif "contentBlockStart" in data:
        import aws_sdk_bedrock_runtime.types.content_block_start_event

        return {
            "contentBlockStart": aws_sdk_bedrock_runtime.types.content_block_start_event.deserialize_json(
                data["contentBlockStart"]
            )
        }
    elif "contentBlockDelta" in data:
        import aws_sdk_bedrock_runtime.types.content_block_delta_event

        return {
            "contentBlockDelta": aws_sdk_bedrock_runtime.types.content_block_delta_event.deserialize_json(
                data["contentBlockDelta"]
            )
        }
    elif "contentBlockStop" in data:
        import aws_sdk_bedrock_runtime.types.content_block_stop_event

        return {
            "contentBlockStop": aws_sdk_bedrock_runtime.types.content_block_stop_event.deserialize_json(
                data["contentBlockStop"]
            )
        }
    elif "messageStop" in data:
        import aws_sdk_bedrock_runtime.types.message_stop_event

        return {
            "messageStop": aws_sdk_bedrock_runtime.types.message_stop_event.deserialize_json(
                data["messageStop"]
            )
        }
    elif "metadata" in data:
        import aws_sdk_bedrock_runtime.types.converse_stream_metadata_event

        return {
            "metadata": aws_sdk_bedrock_runtime.types.converse_stream_metadata_event.deserialize_json(
                data["metadata"]
            )
        }
    elif "internalServerException" in data:
        import aws_sdk_bedrock_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_runtime.errors.internal_server_exception.deserialize_json(
                data["internalServerException"]
            )
        }
    elif "modelStreamErrorException" in data:
        import aws_sdk_bedrock_runtime.errors.model_stream_error_exception

        return {
            "modelStreamErrorException": aws_sdk_bedrock_runtime.errors.model_stream_error_exception.deserialize_json(
                data["modelStreamErrorException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_bedrock_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_runtime.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    elif "throttlingException" in data:
        import aws_sdk_bedrock_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_runtime.errors.throttling_exception.deserialize_json(
                data["throttlingException"]
            )
        }
    elif "serviceUnavailableException" in data:
        import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

        return {
            "serviceUnavailableException": aws_sdk_bedrock_runtime.errors.service_unavailable_exception.deserialize_json(
                data["serviceUnavailableException"]
            )
        }
    else:
        raise DeserializationError("ConverseStreamOutput: no recognized variant key")
