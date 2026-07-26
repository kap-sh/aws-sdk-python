"""Generated from Smithy shape ``com.amazonaws.deadline#QueueStatus``."""

from typing import Literal, TypeAlias, cast

QueueStatus: TypeAlias = Literal[
    "IDLE",
    "SCHEDULING",
    "SCHEDULING_BLOCKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueStatus:
    return cast(QueueStatus, data)
