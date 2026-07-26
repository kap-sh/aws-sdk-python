"""Generated from Smithy shape ``com.amazonaws.sagemaker#Statistic``."""

from typing import Literal, TypeAlias, cast

Statistic: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
    "SampleCount",
    "Sum",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Statistic:
    return cast(Statistic, data)
