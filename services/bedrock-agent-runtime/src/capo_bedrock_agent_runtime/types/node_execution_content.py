"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeExecutionContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError


class _NodeExecutionContent_document(TypedDict, closed=True):
    document: "object"


NodeExecutionContent: TypeAlias = _NodeExecutionContent_document


# --- restJson1 ser/de ---
def serialize_json(value: NodeExecutionContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("NodeExecutionContent: no variant present")


def deserialize_json(data: dict) -> NodeExecutionContent:
    if "document" in data:
        return {"document": data["document"]}
    else:
        raise DeserializationError("NodeExecutionContent: no recognized variant key")
