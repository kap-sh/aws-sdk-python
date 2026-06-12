"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsMetricDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_metric_dimension

PerformanceInsightsMetricDimensions: TypeAlias = list[
    "aws_sdk_devops_guru.types.performance_insights_metric_dimension.PerformanceInsightsMetricDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsMetricDimensions) -> list:
    return list(value)


def deserialize_json(data: list) -> PerformanceInsightsMetricDimensions:
    return list(data)
