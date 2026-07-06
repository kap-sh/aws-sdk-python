"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockDeltaEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.content_block_delta
    import aws_sdk_bedrock_runtime.types.non_negative_integer


class ContentBlockDeltaEvent(TypedDict, closed=True):
    delta: "aws_sdk_bedrock_runtime.types.content_block_delta.ContentBlockDelta"
    """<p>The delta for a content block delta event.</p>"""
    content_block_index: (
        "aws_sdk_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The block index for a content block delta event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockDeltaEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.content_block_delta

    out["delta"] = aws_sdk_bedrock_runtime.types.content_block_delta.serialize_json(
        value["delta"]
    )
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockDeltaEvent:
    out: ContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if "delta" in data:
        import aws_sdk_bedrock_runtime.types.content_block_delta

        out["delta"] = (
            aws_sdk_bedrock_runtime.types.content_block_delta.deserialize_json(
                data["delta"]
            )
        )
    else:
        raise DeserializationError("ContentBlockDeltaEvent.delta required")
    if "contentBlockIndex" in data:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "ContentBlockDeltaEvent.content_block_index required"
        )
    return out


def serialize_event_json(value: ContentBlockDeltaEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "contentBlockDelta"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ContentBlockDeltaEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    return out
