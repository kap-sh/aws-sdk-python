"""Generated from Smithy shape ``com.amazonaws.appflow#TaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: TaskType) -> str:
    return value


def deserialize_json(data: str) -> TaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskType value: {data!r}")
    return cast(TaskType, data)
