"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.recommendation

RecommendationsList: TypeAlias = list["capo_sesv2.types.recommendation.Recommendation"]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationsList) -> list:
    import capo_sesv2.types.recommendation

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationsList:
    import capo_sesv2.types.recommendation

    out: RecommendationsList = []
    for item in data:
        out.append(capo_sesv2.types.recommendation.deserialize_json(item))
    return out
