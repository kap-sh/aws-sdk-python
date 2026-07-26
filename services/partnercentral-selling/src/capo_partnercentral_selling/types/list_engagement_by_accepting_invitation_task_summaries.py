"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementByAcceptingInvitationTaskSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary

ListEngagementByAcceptingInvitationTaskSummaries: TypeAlias = list[
    "capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary.ListEngagementByAcceptingInvitationTaskSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListEngagementByAcceptingInvitationTaskSummaries,
) -> list:
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ListEngagementByAcceptingInvitationTaskSummaries:
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary

    out: ListEngagementByAcceptingInvitationTaskSummaries = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
