"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedAnomalySourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.recommendation_related_cloud_watch_metrics_source_details


class RecommendationRelatedAnomalySourceDetail(TypedDict, closed=True):
    cloud_watch_metrics: NotRequired[
        "aws_sdk_devops_guru.types.recommendation_related_cloud_watch_metrics_source_details.RecommendationRelatedCloudWatchMetricsSourceDetails"
    ]
    """<p> An array of <code>CloudWatchMetricsDetail</code> objects that contains information about the analyzed metrics that displayed anomalous behavior. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedAnomalySourceDetail) -> dict:
    out: dict = {}
    if "cloud_watch_metrics" in value:
        import aws_sdk_devops_guru.types.recommendation_related_cloud_watch_metrics_source_details

        out["CloudWatchMetrics"] = (
            aws_sdk_devops_guru.types.recommendation_related_cloud_watch_metrics_source_details.serialize_json(
                value["cloud_watch_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationRelatedAnomalySourceDetail:
    out: RecommendationRelatedAnomalySourceDetail = {}  # type: ignore[typeddict-item]
    if "CloudWatchMetrics" in data:
        import aws_sdk_devops_guru.types.recommendation_related_cloud_watch_metrics_source_details

        out["cloud_watch_metrics"] = (
            aws_sdk_devops_guru.types.recommendation_related_cloud_watch_metrics_source_details.deserialize_json(
                data["CloudWatchMetrics"]
            )
        )
    return out
