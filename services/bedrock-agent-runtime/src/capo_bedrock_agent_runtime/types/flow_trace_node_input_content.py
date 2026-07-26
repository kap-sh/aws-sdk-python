"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError


class _FlowTraceNodeInputContent_document(TypedDict, closed=True):
    document: "object"


FlowTraceNodeInputContent: TypeAlias = _FlowTraceNodeInputContent_document


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowTraceNodeInputContent: no variant present")


def deserialize_json(data: dict) -> FlowTraceNodeInputContent:
    if "document" in data:
        return {"document": data["document"]}
    else:
        raise DeserializationError(
            "FlowTraceNodeInputContent: no recognized variant key"
        )
