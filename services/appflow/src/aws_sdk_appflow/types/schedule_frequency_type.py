"""Generated from Smithy shape ``com.amazonaws.appflow#ScheduleFrequencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

ScheduleFrequencyType: TypeAlias = Literal[
    "BYMINUTE",
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "ONCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BYMINUTE",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "ONCE",
    )
)


def serialize_json(value: ScheduleFrequencyType) -> str:
    return value


def deserialize_json(data: str) -> ScheduleFrequencyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleFrequencyType value: {data!r}")
    return cast(ScheduleFrequencyType, data)
