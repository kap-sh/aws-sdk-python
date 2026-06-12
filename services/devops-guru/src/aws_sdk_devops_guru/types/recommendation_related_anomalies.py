"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedAnomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.recommendation_related_anomaly

RecommendationRelatedAnomalies: TypeAlias = list[
    "aws_sdk_devops_guru.types.recommendation_related_anomaly.RecommendationRelatedAnomaly"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedAnomalies) -> list:
    import aws_sdk_devops_guru.types.recommendation_related_anomaly

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_anomaly.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationRelatedAnomalies:
    import aws_sdk_devops_guru.types.recommendation_related_anomaly

    out: RecommendationRelatedAnomalies = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_anomaly.deserialize_json(
                item
            )
        )
    return out
