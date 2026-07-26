"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementByAcceptingInvitationTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summaries


class ListEngagementByAcceptingInvitationTasksResponse(TypedDict, closed=True):
    task_summaries: NotRequired[
        "capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summaries.ListEngagementByAcceptingInvitationTaskSummaries"
    ]
    """<p> An array of <code>EngagementByAcceptingInvitationTaskSummary</code> objects, each representing a task that matches the specified filters. The array may be empty if no tasks match the criteria. </p>"""
    next_token: NotRequired["str"]
    """<p> A token used for pagination to retrieve the next page of results.If there are more results available, this field will contain a token that can be used in a subsequent API call to retrieve the next page. If there are no more results, this field will be null or an empty string. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListEngagementByAcceptingInvitationTasksResponse,
) -> dict:
    out: dict = {}
    if "task_summaries" in value:
        import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summaries

        out["TaskSummaries"] = (
            capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summaries.serialize_aws_json_1_0(
                value["task_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListEngagementByAcceptingInvitationTasksResponse:
    out: ListEngagementByAcceptingInvitationTasksResponse = {}  # type: ignore[typeddict-item]
    if "TaskSummaries" in data:
        import capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summaries

        out["task_summaries"] = (
            capo_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summaries.deserialize_aws_json_1_0(
                data["TaskSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
