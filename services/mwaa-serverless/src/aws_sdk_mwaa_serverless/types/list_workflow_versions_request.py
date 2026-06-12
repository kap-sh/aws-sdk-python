"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListWorkflowVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.workflow_arn


class ListWorkflowVersionsRequest(TypedDict):
    max_results: "int"
    """<p>The maximum number of workflow versions to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowVersions</code>.</p>"""
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow for which you want to list versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkflowVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkflowVersionsRequest:
    out: ListWorkflowVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
