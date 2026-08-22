"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError


class _FlowInputContent_document(TypedDict, closed=True):
    document: "object"


FlowInputContent: TypeAlias = _FlowInputContent_document


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowInputContent: no variant present")


def deserialize_json(data: dict) -> FlowInputContent:
    if data.get("document") is not None:
        return {"document": data["document"]}
    else:
        raise DeserializationError("FlowInputContent: no recognized variant key")
