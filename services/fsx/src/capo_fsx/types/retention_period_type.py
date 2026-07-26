"""Generated from Smithy shape ``com.amazonaws.fsx#RetentionPeriodType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: RetentionPeriodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionPeriodType:
    return cast(RetentionPeriodType, data)
