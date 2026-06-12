"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.double

MetricValues: TypeAlias = list["aws_sdk_sagemaker_metrics.types.double.Double"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricValues) -> list:
    return list(value)


def deserialize_json(data: list) -> MetricValues:
    return list(data)
