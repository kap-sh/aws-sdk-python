"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DescriptorType``."""

from typing import Literal, TypeAlias, cast

"""<p> The type of descriptor associated with a registry record.</p>"""
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
