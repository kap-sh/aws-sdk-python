"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedAnomalyResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.recommendation_related_anomaly_resource

RecommendationRelatedAnomalyResources: TypeAlias = list[
    "aws_sdk_devops_guru.types.recommendation_related_anomaly_resource.RecommendationRelatedAnomalyResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedAnomalyResources) -> list:
    import aws_sdk_devops_guru.types.recommendation_related_anomaly_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_anomaly_resource.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationRelatedAnomalyResources:
    import aws_sdk_devops_guru.types.recommendation_related_anomaly_resource

    out: RecommendationRelatedAnomalyResources = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_anomaly_resource.deserialize_json(
                item
            )
        )
    return out
