"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowMultiTurnInputContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError, SerializationError

class _FlowMultiTurnInputContent_document(TypedDict):
    document: "object"

FlowMultiTurnInputContent: TypeAlias = _FlowMultiTurnInputContent_document

# --- restJson1 ser/de ---
def serialize_json(value: FlowMultiTurnInputContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowMultiTurnInputContent: no variant present")


def deserialize_json(data: dict) -> FlowMultiTurnInputContent:
    if "document" in data:
        return {"document": data["document"]}
    else:
        raise DeserializationError("FlowMultiTurnInputContent: no recognized variant key")