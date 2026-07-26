"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FailedGroupingRecommendationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.failed_grouping_recommendation_entry

FailedGroupingRecommendationEntries: TypeAlias = list[
    "capo_resiliencehub.types.failed_grouping_recommendation_entry.FailedGroupingRecommendationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedGroupingRecommendationEntries) -> list:
    import capo_resiliencehub.types.failed_grouping_recommendation_entry

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehub.types.failed_grouping_recommendation_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailedGroupingRecommendationEntries:
    import capo_resiliencehub.types.failed_grouping_recommendation_entry

    out: FailedGroupingRecommendationEntries = []
    for item in data:
        out.append(
            capo_resiliencehub.types.failed_grouping_recommendation_entry.deserialize_json(
                item
            )
        )
    return out
