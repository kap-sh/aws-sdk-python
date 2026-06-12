"""Generated from Smithy shape ``com.amazonaws.fsx#AutocommitPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

AutocommitPeriodType: TypeAlias = Literal[
    "MINUTES",
    "HOURS",
    "DAYS",
    "MONTHS",
    "YEARS",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MINUTES",
        "HOURS",
        "DAYS",
        "MONTHS",
        "YEARS",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: AutocommitPeriodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutocommitPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutocommitPeriodType value: {data!r}")
    return cast(AutocommitPeriodType, data)
