"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError


class _FlowExecutionContent_document(TypedDict, closed=True):
    document: "object"


FlowExecutionContent: TypeAlias = _FlowExecutionContent_document


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowExecutionContent: no variant present")


def deserialize_json(data: dict) -> FlowExecutionContent:
    if data.get("document") is not None:
        return {"document": data["document"]}
    else:
        raise DeserializationError("FlowExecutionContent: no recognized variant key")
