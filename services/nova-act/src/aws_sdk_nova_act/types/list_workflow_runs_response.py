"""Generated from Smithy shape ``com.amazonaws.novaact#ListWorkflowRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.workflow_run_summaries


class ListWorkflowRunsResponse(TypedDict):
    workflow_run_summaries: (
        "aws_sdk_nova_act.types.workflow_run_summaries.WorkflowRunSummaries"
    )
    """<p>A list of summary information for workflow runs.</p>"""
    next_token: NotRequired["aws_sdk_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowRunsResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.workflow_run_summaries

    out["workflowRunSummaries"] = (
        aws_sdk_nova_act.types.workflow_run_summaries.serialize_json(
            value["workflow_run_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowRunsResponse:
    out: ListWorkflowRunsResponse = {}  # type: ignore[typeddict-item]
    if "workflowRunSummaries" in data:
        import aws_sdk_nova_act.types.workflow_run_summaries

        out["workflow_run_summaries"] = (
            aws_sdk_nova_act.types.workflow_run_summaries.deserialize_json(
                data["workflowRunSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkflowRunsResponse.workflow_run_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
