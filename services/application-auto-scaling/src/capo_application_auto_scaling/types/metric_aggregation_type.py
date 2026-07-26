"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#MetricAggregationType``."""

from typing import Literal, TypeAlias, cast

MetricAggregationType: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAggregationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricAggregationType:
    return cast(MetricAggregationType, data)
