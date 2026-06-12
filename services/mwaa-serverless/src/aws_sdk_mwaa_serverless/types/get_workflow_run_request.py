"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetWorkflowRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.workflow_arn


class GetWorkflowRunRequest(TypedDict):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>"""
    run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowRunRequest:
    out: GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    return out
