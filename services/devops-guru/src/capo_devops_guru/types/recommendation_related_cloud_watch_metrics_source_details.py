"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedCloudWatchMetricsSourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_detail

RecommendationRelatedCloudWatchMetricsSourceDetails: TypeAlias = list[
    "capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_detail.RecommendationRelatedCloudWatchMetricsSourceDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedCloudWatchMetricsSourceDetails) -> list:
    import capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_detail

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationRelatedCloudWatchMetricsSourceDetails:
    import capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_detail

    out: RecommendationRelatedCloudWatchMetricsSourceDetails = []
    for item in data:
        out.append(
            capo_devops_guru.types.recommendation_related_cloud_watch_metrics_source_detail.deserialize_json(
                item
            )
        )
    return out
