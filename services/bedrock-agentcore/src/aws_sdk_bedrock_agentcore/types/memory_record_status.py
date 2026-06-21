"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordStatus``."""

from typing import Literal, TypeAlias, cast

MemoryRecordStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> MemoryRecordStatus:
    return cast(MemoryRecordStatus, data)
