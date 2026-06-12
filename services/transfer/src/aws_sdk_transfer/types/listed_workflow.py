"""Generated from Smithy shape ``com.amazonaws.transfer#ListedWorkflow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.workflow_description
    import aws_sdk_transfer.types.workflow_id


class ListedWorkflow(TypedDict):
    workflow_id: NotRequired["aws_sdk_transfer.types.workflow_id.WorkflowId"]
    """<p>A unique identifier for the workflow.</p>"""
    description: NotRequired[
        "aws_sdk_transfer.types.workflow_description.WorkflowDescription"
    ]
    """<p>Specifies the text description for the workflow.</p>"""
    arn: NotRequired["aws_sdk_transfer.types.arn.Arn"]
    """<p>Specifies the unique Amazon Resource Name (ARN) for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedWorkflow) -> dict:
    out: dict = {}
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedWorkflow:
    out: ListedWorkflow = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
