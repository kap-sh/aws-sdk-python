"""Generated from Smithy shape ``com.amazonaws.connect#RecurrenceFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RecurrenceFrequency: TypeAlias = Literal[
    "WEEKLY",
    "MONTHLY",
    "YEARLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
    )
)


def serialize_json(value: RecurrenceFrequency) -> str:
    return value


def deserialize_json(data: str) -> RecurrenceFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecurrenceFrequency value: {data!r}")
    return cast(RecurrenceFrequency, data)
