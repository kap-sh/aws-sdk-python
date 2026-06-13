"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_resource_summary

RecommendationResourceSummaryList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.recommendation_resource_summary.RecommendationResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceSummaryList) -> list:
    import aws_sdk_trustedadvisor.types.recommendation_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_trustedadvisor.types.recommendation_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationResourceSummaryList:
    import aws_sdk_trustedadvisor.types.recommendation_resource_summary

    out: RecommendationResourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_trustedadvisor.types.recommendation_resource_summary.deserialize_json(
                item
            )
        )
    return out
