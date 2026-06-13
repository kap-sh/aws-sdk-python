"""Generated from Smithy shape ``com.amazonaws.odb#MonthName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

MonthName: TypeAlias = Literal[
    "JANUARY",
    "FEBRUARY",
    "MARCH",
    "APRIL",
    "MAY",
    "JUNE",
    "JULY",
    "AUGUST",
    "SEPTEMBER",
    "OCTOBER",
    "NOVEMBER",
    "DECEMBER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    )
)


def serialize_aws_json_1_0(value: MonthName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MonthName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonthName value: {data!r}")
    return cast(MonthName, data)
