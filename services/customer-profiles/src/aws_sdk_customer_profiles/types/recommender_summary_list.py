"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_summary

RecommenderSummaryList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.recommender_summary.RecommenderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSummaryList) -> list:
    import aws_sdk_customer_profiles.types.recommender_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.recommender_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommenderSummaryList:
    import aws_sdk_customer_profiles.types.recommender_summary

    out: RecommenderSummaryList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.recommender_summary.deserialize_json(item)
        )
    return out
