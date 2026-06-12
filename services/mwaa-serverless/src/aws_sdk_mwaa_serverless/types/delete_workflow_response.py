"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#DeleteWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_version


class DeleteWorkflowResponse(TypedDict):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the deleted workflow.</p>"""
    workflow_version: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version of the workflow that was deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteWorkflowResponse:
    out: DeleteWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("DeleteWorkflowResponse.workflow_arn required")
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    return out
