"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

MemoryStrategyStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: MemoryStrategyStatus) -> str:
    return value


def deserialize_json(data: str) -> MemoryStrategyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryStrategyStatus value: {data!r}")
    return cast(MemoryStrategyStatus, data)
