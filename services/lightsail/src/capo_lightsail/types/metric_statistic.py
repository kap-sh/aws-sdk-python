"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

MetricStatistic: TypeAlias = Literal[
    "Minimum",
    "Maximum",
    "Sum",
    "Average",
    "SampleCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricStatistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricStatistic:
    return cast(MetricStatistic, data)
