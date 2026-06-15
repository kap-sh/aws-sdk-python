"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

MemoryStrategyType: TypeAlias = Literal[
    "SEMANTIC",
    "SUMMARIZATION",
    "USER_PREFERENCE",
    "CUSTOM",
    "EPISODIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEMANTIC",
        "SUMMARIZATION",
        "USER_PREFERENCE",
        "CUSTOM",
        "EPISODIC",
    )
)


def serialize_json(value: MemoryStrategyType) -> str:
    return value


def deserialize_json(data: str) -> MemoryStrategyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemoryStrategyType value: {data!r}")
    return cast(MemoryStrategyType, data)
