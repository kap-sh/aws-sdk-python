"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

MetricStatistic: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
    "SampleCount",
    "Sum",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricStatistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricStatistic:
    return cast(MetricStatistic, data)
