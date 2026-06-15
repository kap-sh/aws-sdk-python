"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "SYSTEM",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM",
        "CUSTOM",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
