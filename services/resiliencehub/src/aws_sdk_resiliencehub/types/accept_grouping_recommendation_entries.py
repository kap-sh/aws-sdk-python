"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AcceptGroupingRecommendationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.accept_grouping_recommendation_entry

AcceptGroupingRecommendationEntries: TypeAlias = list[
    "aws_sdk_resiliencehub.types.accept_grouping_recommendation_entry.AcceptGroupingRecommendationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptGroupingRecommendationEntries) -> list:
    import aws_sdk_resiliencehub.types.accept_grouping_recommendation_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.accept_grouping_recommendation_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AcceptGroupingRecommendationEntries:
    import aws_sdk_resiliencehub.types.accept_grouping_recommendation_entry

    out: AcceptGroupingRecommendationEntries = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.accept_grouping_recommendation_entry.deserialize_json(
                item
            )
        )
    return out
