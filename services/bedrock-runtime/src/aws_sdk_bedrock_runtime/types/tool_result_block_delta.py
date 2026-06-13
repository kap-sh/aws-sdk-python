"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultBlockDelta``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError


class _ToolResultBlockDelta_text(TypedDict):
    text: "str"


class _ToolResultBlockDelta_json(TypedDict):
    json: "object"


ToolResultBlockDelta: TypeAlias = (
    _ToolResultBlockDelta_text | _ToolResultBlockDelta_json
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultBlockDelta) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("ToolResultBlockDelta: no variant present")


def deserialize_json(data: dict) -> ToolResultBlockDelta:
    if "text" in data:
        return {"text": data["text"]}
    elif "json" in data:
        return {"json": data["json"]}
    else:
        raise DeserializationError("ToolResultBlockDelta: no recognized variant key")
