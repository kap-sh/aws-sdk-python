"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetTaskInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.workflow_arn


class GetTaskInstanceRequest(TypedDict):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the task instance.</p>"""
    task_instance_id: "aws_sdk_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the task instance to retrieve.</p>"""
    run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run that contains the task instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTaskInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTaskInstanceRequest:
    out: GetTaskInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
