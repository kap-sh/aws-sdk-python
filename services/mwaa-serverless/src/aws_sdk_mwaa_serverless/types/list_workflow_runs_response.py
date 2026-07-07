"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListWorkflowRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.workflow_run_summaries


class ListWorkflowRunsResponse(TypedDict, closed=True):
    workflow_runs: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_run_summaries.WorkflowRunSummaries"
    ]
    """<p>A list of workflow run summaries for the specified workflow.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkflowRunsResponse) -> dict:
    out: dict = {}
    if "workflow_runs" in value:
        import aws_sdk_mwaa_serverless.types.workflow_run_summaries

        out["WorkflowRuns"] = (
            aws_sdk_mwaa_serverless.types.workflow_run_summaries.serialize_aws_json_1_0(
                value["workflow_runs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkflowRunsResponse:
    out: ListWorkflowRunsResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowRuns" in data:
        import aws_sdk_mwaa_serverless.types.workflow_run_summaries

        out["workflow_runs"] = (
            aws_sdk_mwaa_serverless.types.workflow_run_summaries.deserialize_aws_json_1_0(
                data["WorkflowRuns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
