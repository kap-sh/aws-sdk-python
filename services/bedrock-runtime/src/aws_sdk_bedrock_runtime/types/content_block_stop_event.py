"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockStopEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.non_negative_integer


class ContentBlockStopEvent(TypedDict):
    content_block_index: (
        "aws_sdk_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The index for a content block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockStopEvent) -> dict:
    out: dict = {}
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockStopEvent:
    out: ContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if "contentBlockIndex" in data:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError("ContentBlockStopEvent.content_block_index required")
    return out


def serialize_event_json(value: ContentBlockStopEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "contentBlockStop"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ContentBlockStopEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    return out
