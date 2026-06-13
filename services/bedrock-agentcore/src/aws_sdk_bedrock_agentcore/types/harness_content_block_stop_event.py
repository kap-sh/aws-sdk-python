"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockStopEvent``."""

from typing import TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError

class HarnessContentBlockStopEvent(TypedDict):
    content_block_index: "int"
    """<p>The index of the content block that ended.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockStopEvent) -> dict:
    out: dict = {}
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> HarnessContentBlockStopEvent:
    out: HarnessContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if "contentBlockIndex" in data:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError("HarnessContentBlockStopEvent.content_block_index required")
    return out