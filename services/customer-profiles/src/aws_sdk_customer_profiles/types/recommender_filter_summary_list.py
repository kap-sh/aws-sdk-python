"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilterSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_filter_summary

RecommenderFilterSummaryList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.recommender_filter_summary.RecommenderFilterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderFilterSummaryList) -> list:
    import aws_sdk_customer_profiles.types.recommender_filter_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.recommender_filter_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommenderFilterSummaryList:
    import aws_sdk_customer_profiles.types.recommender_filter_summary

    out: RecommenderFilterSummaryList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.recommender_filter_summary.deserialize_json(
                item
            )
        )
    return out
