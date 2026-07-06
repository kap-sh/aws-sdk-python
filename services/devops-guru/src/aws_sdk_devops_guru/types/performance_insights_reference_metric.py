"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsReferenceMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_metric_query


class PerformanceInsightsReferenceMetric(TypedDict, closed=True):
    metric_query: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_metric_query.PerformanceInsightsMetricQuery"
    ]
    """<p>A query to be processed on the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsReferenceMetric) -> dict:
    out: dict = {}
    if "metric_query" in value:
        import aws_sdk_devops_guru.types.performance_insights_metric_query

        out["MetricQuery"] = (
            aws_sdk_devops_guru.types.performance_insights_metric_query.serialize_json(
                value["metric_query"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceInsightsReferenceMetric:
    out: PerformanceInsightsReferenceMetric = {}  # type: ignore[typeddict-item]
    if "MetricQuery" in data:
        import aws_sdk_devops_guru.types.performance_insights_metric_query

        out["metric_query"] = (
            aws_sdk_devops_guru.types.performance_insights_metric_query.deserialize_json(
                data["MetricQuery"]
            )
        )
    return out
