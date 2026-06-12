"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Arithmetic",
        "Filter",
        "Map",
        "Mask",
        "Merge",
        "Truncate",
        "Validate",
    )
)


def serialize_json(value: TaskType) -> str:
    return value


def deserialize_json(data: str) -> TaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskType value: {data!r}")
    return cast(TaskType, data)
