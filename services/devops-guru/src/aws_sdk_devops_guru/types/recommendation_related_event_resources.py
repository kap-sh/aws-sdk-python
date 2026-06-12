"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedEventResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.recommendation_related_event_resource

RecommendationRelatedEventResources: TypeAlias = list[
    "aws_sdk_devops_guru.types.recommendation_related_event_resource.RecommendationRelatedEventResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedEventResources) -> list:
    import aws_sdk_devops_guru.types.recommendation_related_event_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_event_resource.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationRelatedEventResources:
    import aws_sdk_devops_guru.types.recommendation_related_event_resource

    out: RecommendationRelatedEventResources = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_event_resource.deserialize_json(
                item
            )
        )
    return out
