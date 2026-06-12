"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.recommendation_related_event

RecommendationRelatedEvents: TypeAlias = list[
    "aws_sdk_devops_guru.types.recommendation_related_event.RecommendationRelatedEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedEvents) -> list:
    import aws_sdk_devops_guru.types.recommendation_related_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendationRelatedEvents:
    import aws_sdk_devops_guru.types.recommendation_related_event

    out: RecommendationRelatedEvents = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.recommendation_related_event.deserialize_json(
                item
            )
        )
    return out
