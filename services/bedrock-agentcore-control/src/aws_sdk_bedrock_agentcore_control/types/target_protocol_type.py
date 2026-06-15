"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetProtocolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

TargetProtocolType: TypeAlias = Literal[
    "MCP",
    "HTTP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MCP",
        "HTTP",
    )
)


def serialize_json(value: TargetProtocolType) -> str:
    return value


def deserialize_json(data: str) -> TargetProtocolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetProtocolType value: {data!r}")
    return cast(TargetProtocolType, data)
