"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedAnomalyResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_related_anomaly_resource

RecommendationRelatedAnomalyResources: TypeAlias = list[
    "capo_devops_guru.types.recommendation_related_anomaly_resource.RecommendationRelatedAnomalyResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedAnomalyResources) -> list:
    import capo_devops_guru.types.recommendation_related_anomaly_resource

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.recommendation_related_anomaly_resource.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationRelatedAnomalyResources:
    import capo_devops_guru.types.recommendation_related_anomaly_resource

    out: RecommendationRelatedAnomalyResources = []
    for item in data:
        out.append(
            capo_devops_guru.types.recommendation_related_anomaly_resource.deserialize_json(
                item
            )
        )
    return out
