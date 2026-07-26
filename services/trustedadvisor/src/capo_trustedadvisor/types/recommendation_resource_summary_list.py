"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_resource_summary

RecommendationResourceSummaryList: TypeAlias = list[
    "capo_trustedadvisor.types.recommendation_resource_summary.RecommendationResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceSummaryList) -> list:
    import capo_trustedadvisor.types.recommendation_resource_summary

    out: list = []
    for item in value:
        out.append(
            capo_trustedadvisor.types.recommendation_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationResourceSummaryList:
    import capo_trustedadvisor.types.recommendation_resource_summary

    out: RecommendationResourceSummaryList = []
    for item in data:
        out.append(
            capo_trustedadvisor.types.recommendation_resource_summary.deserialize_json(
                item
            )
        )
    return out
