"""Generated from Smithy shape ``com.amazonaws.kendra#Interval``."""

from typing import Literal, TypeAlias, cast

Interval: TypeAlias = Literal[
    "THIS_MONTH",
    "THIS_WEEK",
    "ONE_WEEK_AGO",
    "TWO_WEEKS_AGO",
    "ONE_MONTH_AGO",
    "TWO_MONTHS_AGO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Interval) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Interval:
    return cast(Interval, data)
