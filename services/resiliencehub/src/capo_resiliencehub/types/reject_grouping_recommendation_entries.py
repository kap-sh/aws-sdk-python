"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RejectGroupingRecommendationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.reject_grouping_recommendation_entry

RejectGroupingRecommendationEntries: TypeAlias = list[
    "capo_resiliencehub.types.reject_grouping_recommendation_entry.RejectGroupingRecommendationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: RejectGroupingRecommendationEntries) -> list:
    import capo_resiliencehub.types.reject_grouping_recommendation_entry

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehub.types.reject_grouping_recommendation_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RejectGroupingRecommendationEntries:
    import capo_resiliencehub.types.reject_grouping_recommendation_entry

    out: RejectGroupingRecommendationEntries = []
    for item in data:
        out.append(
            capo_resiliencehub.types.reject_grouping_recommendation_entry.deserialize_json(
                item
            )
        )
    return out
