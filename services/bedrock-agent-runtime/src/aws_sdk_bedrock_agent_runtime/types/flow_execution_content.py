"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError, SerializationError

class _FlowExecutionContent_document(TypedDict):
    document: "object"

FlowExecutionContent: TypeAlias = _FlowExecutionContent_document

# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowExecutionContent: no variant present")


def deserialize_json(data: dict) -> FlowExecutionContent:
    if "document" in data:
        return {"document": data["document"]}
    else:
        raise DeserializationError("FlowExecutionContent: no recognized variant key")