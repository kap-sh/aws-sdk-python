"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DescriptorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p> The type of descriptor associated with a registry record.</p>"""
DescriptorType: TypeAlias = Literal[
    "MCP",
    "A2A",
    "CUSTOM",
    "AGENT_SKILLS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MCP",
        "A2A",
        "CUSTOM",
        "AGENT_SKILLS",
    )
)


def serialize_json(value: DescriptorType) -> str:
    return value


def deserialize_json(data: str) -> DescriptorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DescriptorType value: {data!r}")
    return cast(DescriptorType, data)
