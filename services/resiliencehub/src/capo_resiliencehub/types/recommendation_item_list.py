"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.recommendation_item

RecommendationItemList: TypeAlias = list[
    "capo_resiliencehub.types.recommendation_item.RecommendationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationItemList) -> list:
    import capo_resiliencehub.types.recommendation_item

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.recommendation_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationItemList:
    import capo_resiliencehub.types.recommendation_item

    out: RecommendationItemList = []
    for item in data:
        out.append(capo_resiliencehub.types.recommendation_item.deserialize_json(item))
    return out
