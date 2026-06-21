"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricSetSource``."""

from typing import Literal, TypeAlias, cast

MetricSetSource: TypeAlias = Literal[
    "Train",
    "Validation",
    "Test",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricSetSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricSetSource:
    return cast(MetricSetSource, data)
