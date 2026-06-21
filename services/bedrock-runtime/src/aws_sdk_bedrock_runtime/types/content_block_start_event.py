"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockStartEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.content_block_start
    import aws_sdk_bedrock_runtime.types.non_negative_integer


class ContentBlockStartEvent(TypedDict):
    start: "aws_sdk_bedrock_runtime.types.content_block_start.ContentBlockStart"
    """<p>Start information about a content block start event. </p>"""
    content_block_index: (
        "aws_sdk_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The index for a content block start event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockStartEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.content_block_start

    out["start"] = aws_sdk_bedrock_runtime.types.content_block_start.serialize_json(
        value["start"]
    )
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockStartEvent:
    out: ContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import aws_sdk_bedrock_runtime.types.content_block_start

        out["start"] = (
            aws_sdk_bedrock_runtime.types.content_block_start.deserialize_json(
                data["start"]
            )
        )
    else:
        raise DeserializationError("ContentBlockStartEvent.start required")
    if "contentBlockIndex" in data:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "ContentBlockStartEvent.content_block_index required"
        )
    return out


def serialize_event_json(value: ContentBlockStartEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "contentBlockStart"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ContentBlockStartEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    return out
