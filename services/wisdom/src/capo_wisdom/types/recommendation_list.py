"""Generated from Smithy shape ``com.amazonaws.wisdom#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.recommendation_data

RecommendationList: TypeAlias = list[
    "capo_wisdom.types.recommendation_data.RecommendationData"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationList) -> list:
    import capo_wisdom.types.recommendation_data

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.recommendation_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationList:
    import capo_wisdom.types.recommendation_data

    out: RecommendationList = []
    for item in data:
        out.append(capo_wisdom.types.recommendation_data.deserialize_json(item))
    return out
