"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListWorkflowRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.version_id
    import aws_sdk_mwaa_serverless.types.workflow_arn


class ListWorkflowRunsRequest(TypedDict, closed=True):
    max_results: "int"
    """<p>The maximum number of workflow runs to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowRuns</code>.</p>"""
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.</p>"""
    workflow_version: NotRequired["aws_sdk_mwaa_serverless.types.version_id.VersionId"]
    """<p>Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkflowRunsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkflowRunsRequest:
    out: ListWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
    return out
