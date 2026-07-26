"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolInputSchema``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError


class _ToolInputSchema_json(TypedDict, closed=True):
    json: "object"


ToolInputSchema: TypeAlias = _ToolInputSchema_json


# --- restJson1 ser/de ---
def serialize_json(value: ToolInputSchema) -> dict:
    if "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("ToolInputSchema: no variant present")


def deserialize_json(data: dict) -> ToolInputSchema:
    if "json" in data:
        return {"json": data["json"]}
    else:
        raise DeserializationError("ToolInputSchema: no recognized variant key")
