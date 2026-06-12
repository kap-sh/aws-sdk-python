"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementFromOpportunityTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summaries


class ListEngagementFromOpportunityTasksResponse(TypedDict):
    task_summaries: NotRequired[
        "aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summaries.ListEngagementFromOpportunityTaskSummaries"
    ]
    """<p> TaskSummaries An array of TaskSummary objects containing details about each task. </p>"""
    next_token: NotRequired["str"]
    """<p> A token used for pagination to retrieve the next page of results. If there are more results available, this field will contain a token that can be used in a subsequent API call to retrieve the next page. If there are no more results, this field will be null or an empty string. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementFromOpportunityTasksResponse) -> dict:
    out: dict = {}
    if "task_summaries" in value:
        import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summaries

        out["TaskSummaries"] = (
            aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summaries.serialize_aws_json_1_0(
                value["task_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementFromOpportunityTasksResponse:
    out: ListEngagementFromOpportunityTasksResponse = {}  # type: ignore[typeddict-item]
    if "TaskSummaries" in data:
        import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summaries

        out["task_summaries"] = (
            aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summaries.deserialize_aws_json_1_0(
                data["TaskSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
