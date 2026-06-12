"""Generated from Smithy shape ``com.amazonaws.transfer#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.workflow_description
    import aws_sdk_transfer.types.workflow_steps


class CreateWorkflowRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_transfer.types.workflow_description.WorkflowDescription"
    ]
    """<p>A textual description for the workflow.</p>"""
    steps: "aws_sdk_transfer.types.workflow_steps.WorkflowSteps"
    """<p>Specifies the details for the steps that are in the specified workflow.</p> <p> The <code>TYPE</code> specifies which of the following actions is being taken for this step. </p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul> <note> <p> Currently, copying and tagging are supported only on S3. </p> </note> <p> For file location, you specify either the Amazon S3 bucket and key, or the Amazon EFS file system ID and path. </p>"""
    on_exception_steps: NotRequired[
        "aws_sdk_transfer.types.workflow_steps.WorkflowSteps"
    ]
    """<p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p> <note> <p>For custom steps, the Lambda function needs to send <code>FAILURE</code> to the call back API to kick off the exception steps. Additionally, if the Lambda does not send <code>SUCCESS</code> before it times out, the exception steps are executed.</p> </note>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
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
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Steps" in data:
        import aws_sdk_transfer.types.workflow_steps

        out["steps"] = aws_sdk_transfer.types.workflow_steps.deserialize_aws_json_1_1(
            data["Steps"]
        )
    else:
        raise DeserializationError("CreateWorkflowRequest.steps required")
    if "OnExceptionSteps" in data:
        import aws_sdk_transfer.types.workflow_steps

        out["on_exception_steps"] = (
            aws_sdk_transfer.types.workflow_steps.deserialize_aws_json_1_1(
                data["OnExceptionSteps"]
            )
        )
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
