"""Generated from Smithy shape ``com.amazonaws.quicksight#DayOfTheWeek``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DayOfTheWeek: TypeAlias = Literal[
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


def serialize_json(value: DayOfTheWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfTheWeek:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DayOfTheWeek value: {data!r}")
    return cast(DayOfTheWeek, data)
