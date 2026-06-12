"""Generated from Smithy shape ``com.amazonaws.forecast#Month``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

Month: TypeAlias = Literal[
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


# --- awsJson1_1 ser/de ---
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


def serialize_aws_json_1_1(value: Month) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Month:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Month value: {data!r}")
    return cast(Month, data)
