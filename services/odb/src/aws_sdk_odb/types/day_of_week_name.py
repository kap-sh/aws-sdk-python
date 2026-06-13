"""Generated from Smithy shape ``com.amazonaws.odb#DayOfWeekName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DayOfWeekName: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- awsJson1_0 ser/de ---
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


def serialize_aws_json_1_0(value: DayOfWeekName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DayOfWeekName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DayOfWeekName value: {data!r}")
    return cast(DayOfWeekName, data)
