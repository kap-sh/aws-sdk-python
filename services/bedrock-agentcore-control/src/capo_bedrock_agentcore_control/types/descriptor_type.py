"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DescriptorType``."""

from typing import Literal, TypeAlias, cast

DescriptorType: TypeAlias = Literal[
    "MCP",
    "A2A",
    "CUSTOM",
    "AGENT_SKILLS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DescriptorType) -> str:
    return value


def deserialize_json(data: str) -> DescriptorType:
    return cast(DescriptorType, data)
