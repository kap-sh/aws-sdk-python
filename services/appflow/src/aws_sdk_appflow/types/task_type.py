"""Generated from Smithy shape ``com.amazonaws.appflow#TaskType``."""

from typing import Literal, TypeAlias, cast

TaskType: TypeAlias = Literal[
    "Arithmetic",
    "Filter",
    "Map",
    "Map_all",
    "Mask",
    "Merge",
    "Passthrough",
    "Truncate",
    "Validate",
    "Partition",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskType) -> str:
    return value


def deserialize_json(data: str) -> TaskType:
    return cast(TaskType, data)
