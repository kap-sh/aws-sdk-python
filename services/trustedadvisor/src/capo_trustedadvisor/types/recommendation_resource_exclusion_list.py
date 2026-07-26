"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceExclusionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_resource_exclusion

RecommendationResourceExclusionList: TypeAlias = list[
    "capo_trustedadvisor.types.recommendation_resource_exclusion.RecommendationResourceExclusion"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceExclusionList) -> list:
    import capo_trustedadvisor.types.recommendation_resource_exclusion

    out: list = []
    for item in value:
        out.append(
            capo_trustedadvisor.types.recommendation_resource_exclusion.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationResourceExclusionList:
    import capo_trustedadvisor.types.recommendation_resource_exclusion

    out: RecommendationResourceExclusionList = []
    for item in data:
        out.append(
            capo_trustedadvisor.types.recommendation_resource_exclusion.deserialize_json(
                item
            )
        )
    return out
