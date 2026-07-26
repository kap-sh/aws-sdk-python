"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyStatus``."""

from typing import Literal, TypeAlias, cast

MemoryStrategyStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyStatus) -> str:
    return value


def deserialize_json(data: str) -> MemoryStrategyStatus:
    return cast(MemoryStrategyStatus, data)
