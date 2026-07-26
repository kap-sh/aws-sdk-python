"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationPillarList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_pillar

RecommendationPillarList: TypeAlias = list[
    "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationPillarList) -> list:
    import capo_trustedadvisor.types.recommendation_pillar

    out: list = []
    for item in value:
        out.append(capo_trustedadvisor.types.recommendation_pillar.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationPillarList:
    import capo_trustedadvisor.types.recommendation_pillar

    out: RecommendationPillarList = []
    for item in data:
        out.append(
            capo_trustedadvisor.types.recommendation_pillar.deserialize_json(item)
        )
    return out
