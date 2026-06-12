"""Generated from Smithy shape ``com.amazonaws.connect#OverrideDays``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

OverrideDays: TypeAlias = Literal[
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


def serialize_json(value: OverrideDays) -> str:
    return value


def deserialize_json(data: str) -> OverrideDays:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverrideDays value: {data!r}")
    return cast(OverrideDays, data)
