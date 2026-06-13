"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#OrganizationRecommendationResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary

OrganizationRecommendationResourceSummaryList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary.OrganizationRecommendationResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationRecommendationResourceSummaryList) -> list:
    import aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationRecommendationResourceSummaryList:
    import aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary

    out: OrganizationRecommendationResourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary.deserialize_json(
                item
            )
        )
    return out
