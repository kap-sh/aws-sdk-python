"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime._iter import AnyIterator
from aws_sdk_bedrock_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part


class _InvokeModelWithBidirectionalStreamInput_chunk(TypedDict, closed=True):
    chunk: "aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part.BidirectionalInputPayloadPart"


_InvokeModelWithBidirectionalStreamInput: TypeAlias = (
    _InvokeModelWithBidirectionalStreamInput_chunk
)
InvokeModelWithBidirectionalStreamInput: TypeAlias = AnyIterator[
    _InvokeModelWithBidirectionalStreamInput
]


def serialize_event_json(value: _InvokeModelWithBidirectionalStreamInput) -> bytes:
    match value:
        case {"chunk": payload}:
            import aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part

            return aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamInput: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message,
) -> _InvokeModelWithBidirectionalStreamInput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "chunk":
            import aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part

            return {
                "chunk": aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamInput: unrecognized event-type {event_type!r}"
            )
