"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TaskType``."""

from typing import Literal, TypeAlias, cast

TaskType: TypeAlias = Literal[
    "Arithmetic",
    "Filter",
    "Map",
    "Mask",
    "Merge",
    "Truncate",
    "Validate",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskType) -> str:
    return value


def deserialize_json(data: str) -> TaskType:
    return cast(TaskType, data)
