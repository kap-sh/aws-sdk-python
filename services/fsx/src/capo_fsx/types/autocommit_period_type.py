"""Generated from Smithy shape ``com.amazonaws.fsx#AutocommitPeriodType``."""

from typing import Literal, TypeAlias, cast

AutocommitPeriodType: TypeAlias = Literal[
    "MINUTES",
    "HOURS",
    "DAYS",
    "MONTHS",
    "YEARS",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutocommitPeriodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutocommitPeriodType:
    return cast(AutocommitPeriodType, data)
