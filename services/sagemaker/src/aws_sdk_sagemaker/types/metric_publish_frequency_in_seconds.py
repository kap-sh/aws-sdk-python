"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricPublishFrequencyInSeconds``."""

from typing import Literal, TypeAlias, cast

MetricPublishFrequencyInSeconds: TypeAlias = Literal[
    10,
    30,
    60,
    120,
    180,
    240,
    300,
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricPublishFrequencyInSeconds) -> int:
    return value


def deserialize_aws_json_1_1(data: int) -> MetricPublishFrequencyInSeconds:
    return cast(MetricPublishFrequencyInSeconds, data)
