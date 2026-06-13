"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Day``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Day: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    )
)


def serialize_json(value: Day) -> str:
    return value


def deserialize_json(data: str) -> Day:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Day value: {data!r}")
    return cast(Day, data)
