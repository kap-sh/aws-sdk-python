"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionStepResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.execution_error
    import aws_sdk_transfer.types.step_result_outputs_json
    import aws_sdk_transfer.types.workflow_step_type


class ExecutionStepResult(TypedDict, closed=True):
    step_type: NotRequired["aws_sdk_transfer.types.workflow_step_type.WorkflowStepType"]
    """<p>One of the available step types.</p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul>"""
    outputs: NotRequired[
        "aws_sdk_transfer.types.step_result_outputs_json.StepResultOutputsJson"
    ]
    """<p>The values for the key/value pair applied as a tag to the file. Only applicable if the step type is <code>TAG</code>.</p>"""
    error: NotRequired["aws_sdk_transfer.types.execution_error.ExecutionError"]
    """<p>Specifies the details for an error, if it occurred during execution of the specified workflow step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStepResult) -> dict:
    out: dict = {}
    if "step_type" in value:
        import aws_sdk_transfer.types.workflow_step_type

        out["StepType"] = (
            aws_sdk_transfer.types.workflow_step_type.serialize_aws_json_1_1(
                value["step_type"]
            )
        )
    if "outputs" in value:
        out["Outputs"] = value["outputs"]
    if "error" in value:
        import aws_sdk_transfer.types.execution_error

        out["Error"] = aws_sdk_transfer.types.execution_error.serialize_aws_json_1_1(
            value["error"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionStepResult:
    out: ExecutionStepResult = {}  # type: ignore[typeddict-item]
    if "StepType" in data:
        import aws_sdk_transfer.types.workflow_step_type

        out["step_type"] = (
            aws_sdk_transfer.types.workflow_step_type.deserialize_aws_json_1_1(
                data["StepType"]
            )
        )
    if "Outputs" in data:
        out["outputs"] = data["Outputs"]
    if "Error" in data:
        import aws_sdk_transfer.types.execution_error

        out["error"] = aws_sdk_transfer.types.execution_error.deserialize_aws_json_1_1(
            data["Error"]
        )
    return out
