"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnabledMemoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.memory_type

EnabledMemoryTypes: TypeAlias = list["capo_bedrock_agent.types.memory_type.MemoryType"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledMemoryTypes) -> list:
    import capo_bedrock_agent.types.memory_type

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.memory_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnabledMemoryTypes:
    import capo_bedrock_agent.types.memory_type

    out: EnabledMemoryTypes = []
    for item in data:
        out.append(capo_bedrock_agent.types.memory_type.deserialize_json(item))
    return out
