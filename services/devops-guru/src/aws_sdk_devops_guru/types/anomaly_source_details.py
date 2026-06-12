"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalySourceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.cloud_watch_metrics_details
    import aws_sdk_devops_guru.types.performance_insights_metrics_details


class AnomalySourceDetails(TypedDict):
    cloud_watch_metrics: NotRequired[
        "aws_sdk_devops_guru.types.cloud_watch_metrics_details.CloudWatchMetricsDetails"
    ]
    """<p>An array of <code>CloudWatchMetricsDetail</code> objects that contain information about analyzed CloudWatch metrics that show anomalous behavior. </p>"""
    performance_insights_metrics: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_metrics_details.PerformanceInsightsMetricsDetails"
    ]
    """<p>An array of <code>PerformanceInsightsMetricsDetail</code> objects that contain information about analyzed Performance Insights metrics that show anomalous behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalySourceDetails) -> dict:
    out: dict = {}
    if "cloud_watch_metrics" in value:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_details

        out["CloudWatchMetrics"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_details.serialize_json(
                value["cloud_watch_metrics"]
            )
        )
    if "performance_insights_metrics" in value:
        import aws_sdk_devops_guru.types.performance_insights_metrics_details

        out["PerformanceInsightsMetrics"] = (
            aws_sdk_devops_guru.types.performance_insights_metrics_details.serialize_json(
                value["performance_insights_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnomalySourceDetails:
    out: AnomalySourceDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchMetrics" in data:
        import aws_sdk_devops_guru.types.cloud_watch_metrics_details

        out["cloud_watch_metrics"] = (
            aws_sdk_devops_guru.types.cloud_watch_metrics_details.deserialize_json(
                data["CloudWatchMetrics"]
            )
        )
    if "PerformanceInsightsMetrics" in data:
        import aws_sdk_devops_guru.types.performance_insights_metrics_details

        out["performance_insights_metrics"] = (
            aws_sdk_devops_guru.types.performance_insights_metrics_details.deserialize_json(
                data["PerformanceInsightsMetrics"]
            )
        )
    return out
