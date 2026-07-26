"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SopRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.sop_recommendation

SopRecommendationList: TypeAlias = list[
    "capo_resiliencehub.types.sop_recommendation.SopRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SopRecommendationList) -> list:
    import capo_resiliencehub.types.sop_recommendation

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.sop_recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> SopRecommendationList:
    import capo_resiliencehub.types.sop_recommendation

    out: SopRecommendationList = []
    for item in data:
        out.append(capo_resiliencehub.types.sop_recommendation.deserialize_json(item))
    return out
