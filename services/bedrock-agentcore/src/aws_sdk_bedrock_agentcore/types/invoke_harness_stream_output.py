"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.errors.internal_server_exception
    import aws_sdk_bedrock_agentcore.errors.runtime_client_error
    import aws_sdk_bedrock_agentcore.errors.validation_exception
    import aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event
    import aws_sdk_bedrock_agentcore.types.harness_content_block_start_event
    import aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event
    import aws_sdk_bedrock_agentcore.types.harness_message_start_event
    import aws_sdk_bedrock_agentcore.types.harness_message_stop_event
    import aws_sdk_bedrock_agentcore.types.harness_metadata_event


class _InvokeHarnessStreamOutput_messageStart(TypedDict):
    messageStart: "aws_sdk_bedrock_agentcore.types.harness_message_start_event.HarnessMessageStartEvent"


class _InvokeHarnessStreamOutput_contentBlockStart(TypedDict):
    contentBlockStart: "aws_sdk_bedrock_agentcore.types.harness_content_block_start_event.HarnessContentBlockStartEvent"


class _InvokeHarnessStreamOutput_contentBlockDelta(TypedDict):
    contentBlockDelta: "aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event.HarnessContentBlockDeltaEvent"


class _InvokeHarnessStreamOutput_contentBlockStop(TypedDict):
    contentBlockStop: "aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event.HarnessContentBlockStopEvent"


class _InvokeHarnessStreamOutput_messageStop(TypedDict):
    messageStop: "aws_sdk_bedrock_agentcore.types.harness_message_stop_event.HarnessMessageStopEvent"


class _InvokeHarnessStreamOutput_metadata(TypedDict):
    metadata: (
        "aws_sdk_bedrock_agentcore.types.harness_metadata_event.HarnessMetadataEvent"
    )


class _InvokeHarnessStreamOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _InvokeHarnessStreamOutput_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


class _InvokeHarnessStreamOutput_runtimeClientError(TypedDict):
    runtimeClientError: (
        "aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError_"
    )


InvokeHarnessStreamOutput: TypeAlias = (
    _InvokeHarnessStreamOutput_messageStart
    | _InvokeHarnessStreamOutput_contentBlockStart
    | _InvokeHarnessStreamOutput_contentBlockDelta
    | _InvokeHarnessStreamOutput_contentBlockStop
    | _InvokeHarnessStreamOutput_messageStop
    | _InvokeHarnessStreamOutput_metadata
    | _InvokeHarnessStreamOutput_internalServerException
    | _InvokeHarnessStreamOutput_validationException
    | _InvokeHarnessStreamOutput_runtimeClientError
)


# --- restJson1 ser/de ---
def serialize_json(value: InvokeHarnessStreamOutput) -> dict:
    if "messageStart" in value:
        import aws_sdk_bedrock_agentcore.types.harness_message_start_event

        return {
            "messageStart": aws_sdk_bedrock_agentcore.types.harness_message_start_event.serialize_json(
                value["messageStart"]
            )
        }
    elif "contentBlockStart" in value:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_start_event

        return {
            "contentBlockStart": aws_sdk_bedrock_agentcore.types.harness_content_block_start_event.serialize_json(
                value["contentBlockStart"]
            )
        }
    elif "contentBlockDelta" in value:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event

        return {
            "contentBlockDelta": aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event.serialize_json(
                value["contentBlockDelta"]
            )
        }
    elif "contentBlockStop" in value:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event

        return {
            "contentBlockStop": aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event.serialize_json(
                value["contentBlockStop"]
            )
        }
    elif "messageStop" in value:
        import aws_sdk_bedrock_agentcore.types.harness_message_stop_event

        return {
            "messageStop": aws_sdk_bedrock_agentcore.types.harness_message_stop_event.serialize_json(
                value["messageStop"]
            )
        }
    elif "metadata" in value:
        import aws_sdk_bedrock_agentcore.types.harness_metadata_event

        return {
            "metadata": aws_sdk_bedrock_agentcore.types.harness_metadata_event.serialize_json(
                value["metadata"]
            )
        }
    elif "internalServerException" in value:
        import aws_sdk_bedrock_agentcore.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agentcore.errors.internal_server_exception.serialize_json(
                value["internalServerException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_bedrock_agentcore.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agentcore.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    elif "runtimeClientError" in value:
        import aws_sdk_bedrock_agentcore.errors.runtime_client_error

        return {
            "runtimeClientError": aws_sdk_bedrock_agentcore.errors.runtime_client_error.serialize_json(
                value["runtimeClientError"]
            )
        }
    else:
        raise SerializationError("InvokeHarnessStreamOutput: no variant present")


def deserialize_json(data: dict) -> InvokeHarnessStreamOutput:
    if "messageStart" in data:
        import aws_sdk_bedrock_agentcore.types.harness_message_start_event

        return {
            "messageStart": aws_sdk_bedrock_agentcore.types.harness_message_start_event.deserialize_json(
                data["messageStart"]
            )
        }
    elif "contentBlockStart" in data:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_start_event

        return {
            "contentBlockStart": aws_sdk_bedrock_agentcore.types.harness_content_block_start_event.deserialize_json(
                data["contentBlockStart"]
            )
        }
    elif "contentBlockDelta" in data:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event

        return {
            "contentBlockDelta": aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event.deserialize_json(
                data["contentBlockDelta"]
            )
        }
    elif "contentBlockStop" in data:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event

        return {
            "contentBlockStop": aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event.deserialize_json(
                data["contentBlockStop"]
            )
        }
    elif "messageStop" in data:
        import aws_sdk_bedrock_agentcore.types.harness_message_stop_event

        return {
            "messageStop": aws_sdk_bedrock_agentcore.types.harness_message_stop_event.deserialize_json(
                data["messageStop"]
            )
        }
    elif "metadata" in data:
        import aws_sdk_bedrock_agentcore.types.harness_metadata_event

        return {
            "metadata": aws_sdk_bedrock_agentcore.types.harness_metadata_event.deserialize_json(
                data["metadata"]
            )
        }
    elif "internalServerException" in data:
        import aws_sdk_bedrock_agentcore.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agentcore.errors.internal_server_exception.deserialize_json(
                data["internalServerException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_bedrock_agentcore.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agentcore.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    elif "runtimeClientError" in data:
        import aws_sdk_bedrock_agentcore.errors.runtime_client_error

        return {
            "runtimeClientError": aws_sdk_bedrock_agentcore.errors.runtime_client_error.deserialize_json(
                data["runtimeClientError"]
            )
        }
    else:
        raise DeserializationError(
            "InvokeHarnessStreamOutput: no recognized variant key"
        )
