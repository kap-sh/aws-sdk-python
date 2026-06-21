"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyType``."""

from typing import Literal, TypeAlias, cast

MemoryStrategyType: TypeAlias = Literal[
    "SEMANTIC",
    "SUMMARIZATION",
    "USER_PREFERENCE",
    "CUSTOM",
    "EPISODIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyType) -> str:
    return value


def deserialize_json(data: str) -> MemoryStrategyType:
    return cast(MemoryStrategyType, data)
