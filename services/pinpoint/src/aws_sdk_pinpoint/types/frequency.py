"""Generated from Smithy shape ``com.amazonaws.pinpoint#Frequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Frequency: TypeAlias = Literal[
    "ONCE",
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "EVENT",
    "IN_APP_EVENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONCE",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "EVENT",
        "IN_APP_EVENT",
    )
)


def serialize_json(value: Frequency) -> str:
    return value


def deserialize_json(data: str) -> Frequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Frequency value: {data!r}")
    return cast(Frequency, data)
