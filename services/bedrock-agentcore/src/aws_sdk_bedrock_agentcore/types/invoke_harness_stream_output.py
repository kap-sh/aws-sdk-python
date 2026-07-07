"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore._iter import AnyIterator
from aws_sdk_bedrock_agentcore._protocol.eventstream import Message

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


class _InvokeHarnessStreamOutput_messageStart(TypedDict, closed=True):
    messageStart: "aws_sdk_bedrock_agentcore.types.harness_message_start_event.HarnessMessageStartEvent"


class _InvokeHarnessStreamOutput_contentBlockStart(TypedDict, closed=True):
    contentBlockStart: "aws_sdk_bedrock_agentcore.types.harness_content_block_start_event.HarnessContentBlockStartEvent"


class _InvokeHarnessStreamOutput_contentBlockDelta(TypedDict, closed=True):
    contentBlockDelta: "aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event.HarnessContentBlockDeltaEvent"


class _InvokeHarnessStreamOutput_contentBlockStop(TypedDict, closed=True):
    contentBlockStop: "aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event.HarnessContentBlockStopEvent"


class _InvokeHarnessStreamOutput_messageStop(TypedDict, closed=True):
    messageStop: "aws_sdk_bedrock_agentcore.types.harness_message_stop_event.HarnessMessageStopEvent"


class _InvokeHarnessStreamOutput_metadata(TypedDict, closed=True):
    metadata: (
        "aws_sdk_bedrock_agentcore.types.harness_metadata_event.HarnessMetadataEvent"
    )


class _InvokeHarnessStreamOutput_internalServerException(TypedDict, closed=True):
    internalServerException: "aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _InvokeHarnessStreamOutput_validationException(TypedDict, closed=True):
    validationException: (
        "aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


class _InvokeHarnessStreamOutput_runtimeClientError(TypedDict, closed=True):
    runtimeClientError: (
        "aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError_"
    )


_InvokeHarnessStreamOutput: TypeAlias = (
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
InvokeHarnessStreamOutput: TypeAlias = AnyIterator[_InvokeHarnessStreamOutput]


def serialize_event_json(value: _InvokeHarnessStreamOutput) -> bytes:
    match value:
        case {"messageStart": payload}:
            import aws_sdk_bedrock_agentcore.types.harness_message_start_event

            return aws_sdk_bedrock_agentcore.types.harness_message_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockStart": payload}:
            import aws_sdk_bedrock_agentcore.types.harness_content_block_start_event

            return aws_sdk_bedrock_agentcore.types.harness_content_block_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockDelta": payload}:
            import aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event

            return aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event.serialize_event_json(
                payload
            )
        case {"contentBlockStop": payload}:
            import aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event

            return aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event.serialize_event_json(
                payload
            )
        case {"messageStop": payload}:
            import aws_sdk_bedrock_agentcore.types.harness_message_stop_event

            return aws_sdk_bedrock_agentcore.types.harness_message_stop_event.serialize_event_json(
                payload
            )
        case {"metadata": payload}:
            import aws_sdk_bedrock_agentcore.types.harness_metadata_event

            return aws_sdk_bedrock_agentcore.types.harness_metadata_event.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import aws_sdk_bedrock_agentcore.errors.internal_server_exception

            return aws_sdk_bedrock_agentcore.errors.internal_server_exception.serialize_event_json(
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
                f"InvokeHarnessStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _InvokeHarnessStreamOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "internalServerException":
                import aws_sdk_bedrock_agentcore.errors.internal_server_exception

                raise aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException(
                    aws_sdk_bedrock_agentcore.errors.internal_server_exception.deserialize_event_json(
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
            f"InvokeHarnessStreamOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "messageStart":
            import aws_sdk_bedrock_agentcore.types.harness_message_start_event

            return {
                "messageStart": aws_sdk_bedrock_agentcore.types.harness_message_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStart":
            import aws_sdk_bedrock_agentcore.types.harness_content_block_start_event

            return {
                "contentBlockStart": aws_sdk_bedrock_agentcore.types.harness_content_block_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockDelta":
            import aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event

            return {
                "contentBlockDelta": aws_sdk_bedrock_agentcore.types.harness_content_block_delta_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStop":
            import aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event

            return {
                "contentBlockStop": aws_sdk_bedrock_agentcore.types.harness_content_block_stop_event.deserialize_event_json(
                    message
                )
            }
        case "messageStop":
            import aws_sdk_bedrock_agentcore.types.harness_message_stop_event

            return {
                "messageStop": aws_sdk_bedrock_agentcore.types.harness_message_stop_event.deserialize_event_json(
                    message
                )
            }
        case "metadata":
            import aws_sdk_bedrock_agentcore.types.harness_metadata_event

            return {
                "metadata": aws_sdk_bedrock_agentcore.types.harness_metadata_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeHarnessStreamOutput: unrecognized event-type {event_type!r}"
            )
