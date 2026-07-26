"""Generated from Smithy shape ``com.amazonaws.devopsguru#RelatedAnomalySourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_related_anomaly_source_detail

RelatedAnomalySourceDetails: TypeAlias = list[
    "capo_devops_guru.types.recommendation_related_anomaly_source_detail.RecommendationRelatedAnomalySourceDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedAnomalySourceDetails) -> list:
    import capo_devops_guru.types.recommendation_related_anomaly_source_detail

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.recommendation_related_anomaly_source_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RelatedAnomalySourceDetails:
    import capo_devops_guru.types.recommendation_related_anomaly_source_detail

    out: RelatedAnomalySourceDetails = []
    for item in data:
        out.append(
            capo_devops_guru.types.recommendation_related_anomaly_source_detail.deserialize_json(
                item
            )
        )
    return out
