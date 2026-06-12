"""Generated from Smithy shape ``com.amazonaws.deadline#Period``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

Period: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
    )
)


def serialize_json(value: Period) -> str:
    return value


def deserialize_json(data: str) -> Period:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Period value: {data!r}")
    return cast(Period, data)
