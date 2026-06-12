"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationDays``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

HoursOfOperationDays: TypeAlias = Literal[
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


def serialize_json(value: HoursOfOperationDays) -> str:
    return value


def deserialize_json(data: str) -> HoursOfOperationDays:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HoursOfOperationDays value: {data!r}")
    return cast(HoursOfOperationDays, data)
