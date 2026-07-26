"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_summary

RecommendationSummaryList: TypeAlias = list[
    "capo_trustedadvisor.types.recommendation_summary.RecommendationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSummaryList) -> list:
    import capo_trustedadvisor.types.recommendation_summary

    out: list = []
    for item in value:
        out.append(
            capo_trustedadvisor.types.recommendation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendationSummaryList:
    import capo_trustedadvisor.types.recommendation_summary

    out: RecommendationSummaryList = []
    for item in data:
        out.append(
            capo_trustedadvisor.types.recommendation_summary.deserialize_json(item)
        )
    return out
