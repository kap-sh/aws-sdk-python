"""Generated from Smithy shape ``com.amazonaws.forecast#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

DayOfWeek: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- awsJson1_1 ser/de ---
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


def serialize_aws_json_1_1(value: DayOfWeek) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DayOfWeek:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DayOfWeek value: {data!r}")
    return cast(DayOfWeek, data)
