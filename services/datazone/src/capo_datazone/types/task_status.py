"""Generated from Smithy shape ``com.amazonaws.datazone#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
