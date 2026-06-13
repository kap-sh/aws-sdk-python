"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#OrganizationRecommendationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.organization_recommendation_summary

OrganizationRecommendationSummaryList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.organization_recommendation_summary.OrganizationRecommendationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationRecommendationSummaryList) -> list:
    import aws_sdk_trustedadvisor.types.organization_recommendation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_trustedadvisor.types.organization_recommendation_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationRecommendationSummaryList:
    import aws_sdk_trustedadvisor.types.organization_recommendation_summary

    out: OrganizationRecommendationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_trustedadvisor.types.organization_recommendation_summary.deserialize_json(
                item
            )
        )
    return out
