"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListMatchingWorkflowsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.matching_workflow_list
    import aws_sdk_entityresolution.types.next_token


class ListMatchingWorkflowsOutput(TypedDict):
    workflow_summaries: NotRequired[
        "aws_sdk_entityresolution.types.matching_workflow_list.MatchingWorkflowList"
    ]
    """<p>A list of <code>MatchingWorkflowSummary</code> objects, each of which contain the fields <code>workflowName</code>, <code>workflowArn</code>, <code>resolutionType</code>, <code>createdAt</code>, and <code>updatedAt</code>.</p>"""
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMatchingWorkflowsOutput) -> dict:
    out: dict = {}
    if "workflow_summaries" in value:
        import aws_sdk_entityresolution.types.matching_workflow_list

        out["workflowSummaries"] = (
            aws_sdk_entityresolution.types.matching_workflow_list.serialize_json(
                value["workflow_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMatchingWorkflowsOutput:
    out: ListMatchingWorkflowsOutput = {}  # type: ignore[typeddict-item]
    if "workflowSummaries" in data:
        import aws_sdk_entityresolution.types.matching_workflow_list

        out["workflow_summaries"] = (
            aws_sdk_entityresolution.types.matching_workflow_list.deserialize_json(
                data["workflowSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
