"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStatus``."""

from typing import Literal, TypeAlias, cast

MemoryStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "FAILED",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStatus) -> str:
    return value


def deserialize_json(data: str) -> MemoryStatus:
    return cast(MemoryStatus, data)
