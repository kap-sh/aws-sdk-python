"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWorkflow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.workflow_description
    import aws_sdk_transfer.types.workflow_id
    import aws_sdk_transfer.types.workflow_steps


class DescribedWorkflow(TypedDict):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>Specifies the unique Amazon Resource Name (ARN) for the workflow.</p>"""
    description: NotRequired[
        "aws_sdk_transfer.types.workflow_description.WorkflowDescription"
    ]
    """<p>Specifies the text description for the workflow.</p>"""
    steps: NotRequired["aws_sdk_transfer.types.workflow_steps.WorkflowSteps"]
    """<p>Specifies the details for the steps that are in the specified workflow.</p>"""
    on_exception_steps: NotRequired[
        "aws_sdk_transfer.types.workflow_steps.WorkflowSteps"
    ]
    """<p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p>"""
    workflow_id: NotRequired["aws_sdk_transfer.types.workflow_id.WorkflowId"]
    """<p>A unique identifier for the workflow.</p>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWorkflow) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "steps" in value:
        import aws_sdk_transfer.types.workflow_steps

        out["Steps"] = aws_sdk_transfer.types.workflow_steps.serialize_aws_json_1_1(
            value["steps"]
        )
    if "on_exception_steps" in value:
        import aws_sdk_transfer.types.workflow_steps

        out["OnExceptionSteps"] = (
            aws_sdk_transfer.types.workflow_steps.serialize_aws_json_1_1(
                value["on_exception_steps"]
            )
        )
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedWorkflow:
    out: DescribedWorkflow = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedWorkflow.arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Steps" in data:
        import aws_sdk_transfer.types.workflow_steps

        out["steps"] = aws_sdk_transfer.types.workflow_steps.deserialize_aws_json_1_1(
            data["Steps"]
        )
    if "OnExceptionSteps" in data:
        import aws_sdk_transfer.types.workflow_steps

        out["on_exception_steps"] = (
            aws_sdk_transfer.types.workflow_steps.deserialize_aws_json_1_1(
                data["OnExceptionSteps"]
            )
        )
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
