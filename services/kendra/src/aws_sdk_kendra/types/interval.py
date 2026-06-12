"""Generated from Smithy shape ``com.amazonaws.kendra#Interval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

Interval: TypeAlias = Literal[
    "THIS_MONTH",
    "THIS_WEEK",
    "ONE_WEEK_AGO",
    "TWO_WEEKS_AGO",
    "ONE_MONTH_AGO",
    "TWO_MONTHS_AGO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "THIS_MONTH",
        "THIS_WEEK",
        "ONE_WEEK_AGO",
        "TWO_WEEKS_AGO",
        "ONE_MONTH_AGO",
        "TWO_MONTHS_AGO",
    )
)


def serialize_aws_json_1_1(value: Interval) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Interval:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Interval value: {data!r}")
    return cast(Interval, data)
