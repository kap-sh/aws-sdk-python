"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedCloudWatchMetricsSourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_metric_name
    import capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_namespace


class RecommendationRelatedCloudWatchMetricsSourceDetail(TypedDict, closed=True):
    metric_name: NotRequired[
        "capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_metric_name.RecommendationRelatedCloudWatchMetricsSourceMetricName"
    ]
    """<p>The name of the CloudWatch metric.</p>"""
    namespace: NotRequired[
        "capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_namespace.RecommendationRelatedCloudWatchMetricsSourceNamespace"
    ]
    """<p>The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedCloudWatchMetricsSourceDetail) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> RecommendationRelatedCloudWatchMetricsSourceDetail:
    out: RecommendationRelatedCloudWatchMetricsSourceDetail = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    return out
