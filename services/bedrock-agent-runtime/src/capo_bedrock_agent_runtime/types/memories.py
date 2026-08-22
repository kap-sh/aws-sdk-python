"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Memories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.memory

Memories: TypeAlias = list["capo_bedrock_agent_runtime.types.memory.Memory"]


# --- restJson1 ser/de ---
def serialize_json(value: Memories) -> list:
    import capo_bedrock_agent_runtime.types.memory

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.memory.serialize_json(item))
    return out


def deserialize_json(data: list) -> Memories:
    import capo_bedrock_agent_runtime.types.memory

    out: Memories = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.memory.deserialize_json(item))
    return out
