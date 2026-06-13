"""Generated from Smithy shape ``com.amazonaws.quicksight#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DayOfWeek: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUNDAY",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
    )
)


def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DayOfWeek value: {data!r}")
    return cast(DayOfWeek, data)
