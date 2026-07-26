"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListOpportunityFromEngagementTaskSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary

ListOpportunityFromEngagementTaskSummaries: TypeAlias = list[
    "capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary.ListOpportunityFromEngagementTaskSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpportunityFromEngagementTaskSummaries) -> list:
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListOpportunityFromEngagementTaskSummaries:
    import capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary

    out: ListOpportunityFromEngagementTaskSummaries = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.list_opportunity_from_engagement_task_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
