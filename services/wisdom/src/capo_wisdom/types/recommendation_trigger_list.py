"""Generated from Smithy shape ``com.amazonaws.wisdom#RecommendationTriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.recommendation_trigger

RecommendationTriggerList: TypeAlias = list[
    "capo_wisdom.types.recommendation_trigger.RecommendationTrigger"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTriggerList) -> list:
    import capo_wisdom.types.recommendation_trigger

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.recommendation_trigger.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationTriggerList:
    import capo_wisdom.types.recommendation_trigger

    out: RecommendationTriggerList = []
    for item in data:
        out.append(capo_wisdom.types.recommendation_trigger.deserialize_json(item))
    return out
