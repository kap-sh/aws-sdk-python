"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputContent``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)


class _FlowTraceNodeOutputContent_document(TypedDict):
    document: "object"


FlowTraceNodeOutputContent: TypeAlias = _FlowTraceNodeOutputContent_document


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputContent) -> dict:
    if "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowTraceNodeOutputContent: no variant present")


def deserialize_json(data: dict) -> FlowTraceNodeOutputContent:
    if "document" in data:
        return {"document": data["document"]}
    else:
        raise DeserializationError(
            "FlowTraceNodeOutputContent: no recognized variant key"
        )
