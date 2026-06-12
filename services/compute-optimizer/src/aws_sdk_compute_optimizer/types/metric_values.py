"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.metric_value

MetricValues: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.metric_value.MetricValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> MetricValues:
    return list(data)
