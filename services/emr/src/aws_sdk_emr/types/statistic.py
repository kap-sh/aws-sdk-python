"""Generated from Smithy shape ``com.amazonaws.emr#Statistic``."""

from typing import Literal, TypeAlias, cast

Statistic: TypeAlias = Literal[
    "SAMPLE_COUNT",
    "AVERAGE",
    "SUM",
    "MINIMUM",
    "MAXIMUM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Statistic:
    return cast(Statistic, data)
