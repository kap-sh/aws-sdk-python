"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowOutputContent``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)


class _FlowOutputContent_document(TypedDict):
    document: "object"


FlowOutputContent: TypeAlias = _FlowOutputContent_document


# --- restJson1 ser/de ---
def serialize_json(value: FlowOutputContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowOutputContent: no variant present")


def deserialize_json(data: dict) -> FlowOutputContent:
    if "document" in data:
        return {"document": data["document"]}
    else:
        raise DeserializationError("FlowOutputContent: no recognized variant key")
