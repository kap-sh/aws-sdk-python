"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.workflow_runs


class GetWorkflowRunsResponse(TypedDict, closed=True):
    runs: NotRequired["aws_sdk_glue.types.workflow_runs.WorkflowRuns"]
    """<p>A list of workflow run metadata objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all requested workflow runs have been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunsResponse) -> dict:
    out: dict = {}
    if "runs" in value:
        import aws_sdk_glue.types.workflow_runs

        out["Runs"] = aws_sdk_glue.types.workflow_runs.serialize_aws_json_1_1(
            value["runs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunsResponse:
    out: GetWorkflowRunsResponse = {}  # type: ignore[typeddict-item]
    if "Runs" in data:
        import aws_sdk_glue.types.workflow_runs

        out["runs"] = aws_sdk_glue.types.workflow_runs.deserialize_aws_json_1_1(
            data["Runs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
