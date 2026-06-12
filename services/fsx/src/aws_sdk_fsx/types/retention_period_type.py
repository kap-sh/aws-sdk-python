"""Generated from Smithy shape ``com.amazonaws.fsx#RetentionPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

RetentionPeriodType: TypeAlias = Literal[
    "SECONDS",
    "MINUTES",
    "HOURS",
    "DAYS",
    "MONTHS",
    "YEARS",
    "INFINITE",
    "UNSPECIFIED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECONDS",
        "MINUTES",
        "HOURS",
        "DAYS",
        "MONTHS",
        "YEARS",
        "INFINITE",
        "UNSPECIFIED",
    )
)


def serialize_aws_json_1_1(value: RetentionPeriodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetentionPeriodType value: {data!r}")
    return cast(RetentionPeriodType, data)
