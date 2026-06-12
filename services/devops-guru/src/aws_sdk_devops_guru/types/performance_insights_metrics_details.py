"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsMetricsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_metrics_detail

PerformanceInsightsMetricsDetails: TypeAlias = list[
    "aws_sdk_devops_guru.types.performance_insights_metrics_detail.PerformanceInsightsMetricsDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsMetricsDetails) -> list:
    import aws_sdk_devops_guru.types.performance_insights_metrics_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.performance_insights_metrics_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PerformanceInsightsMetricsDetails:
    import aws_sdk_devops_guru.types.performance_insights_metrics_detail

    out: PerformanceInsightsMetricsDetails = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.performance_insights_metrics_detail.deserialize_json(
                item
            )
        )
    return out
