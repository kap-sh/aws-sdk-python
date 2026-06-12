"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementFromOpportunityTaskSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary

ListEngagementFromOpportunityTaskSummaries: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary.ListEngagementFromOpportunityTaskSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementFromOpportunityTaskSummaries) -> list:
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListEngagementFromOpportunityTaskSummaries:
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary

    out: ListEngagementFromOpportunityTaskSummaries = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
