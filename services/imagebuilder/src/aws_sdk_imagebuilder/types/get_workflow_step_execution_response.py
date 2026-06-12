"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowStepExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.workflow_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_execution_id
    import aws_sdk_imagebuilder.types.workflow_step_action
    import aws_sdk_imagebuilder.types.workflow_step_description
    import aws_sdk_imagebuilder.types.workflow_step_execution_id
    import aws_sdk_imagebuilder.types.workflow_step_execution_rollback_status
    import aws_sdk_imagebuilder.types.workflow_step_execution_status
    import aws_sdk_imagebuilder.types.workflow_step_inputs
    import aws_sdk_imagebuilder.types.workflow_step_message
    import aws_sdk_imagebuilder.types.workflow_step_name
    import aws_sdk_imagebuilder.types.workflow_step_outputs
    import aws_sdk_imagebuilder.types.workflow_step_timeout_seconds_integer


class GetWorkflowStepExecutionResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    step_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    ]
    """<p>The unique identifier for the runtime version of the workflow step that you specified in the request.</p>"""
    workflow_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the build version for the Image Builder workflow resource that defines this workflow step.</p>"""
    workflow_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    ]
    """<p>The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image resource build version that the specified runtime instance of the workflow step creates.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.workflow_step_name.WorkflowStepName"]
    """<p>The name of the specified runtime instance of the workflow step.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_description.WorkflowStepDescription"
    ]
    """<p>Describes the specified workflow step.</p>"""
    action: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_action.WorkflowStepAction"
    ]
    """<p>The name of the action that the specified step performs.</p>"""
    status: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_execution_status.WorkflowStepExecutionStatus"
    ]
    """<p>The current status for the specified runtime version of the workflow step.</p>"""
    rollback_status: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_execution_rollback_status.WorkflowStepExecutionRollbackStatus"
    ]
    """<p>Reports on the rollback status of the specified runtime version of the workflow step, if applicable.</p>"""
    message: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_message.WorkflowStepMessage"
    ]
    """<p>The output message from the specified runtime instance of the workflow step, if applicable.</p>"""
    inputs: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_inputs.WorkflowStepInputs"
    ]
    """<p>Input parameters that Image Builder provided for the specified runtime instance of the workflow step.</p>"""
    outputs: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_outputs.WorkflowStepOutputs"
    ]
    """<p>The file names that the specified runtime version of the workflow step created as output.</p>"""
    start_time: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the specified runtime version of the workflow step started.</p>"""
    end_time: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the specified runtime instance of the workflow step finished.</p>"""
    on_failure: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The action to perform if the workflow step fails.</p>"""
    timeout_seconds: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_timeout_seconds_integer.WorkflowStepTimeoutSecondsInteger"
    ]
    """<p>The maximum duration in seconds for this step to complete its action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepExecutionResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "step_execution_id" in value:
        out["stepExecutionId"] = value["step_execution_id"]
    if "workflow_build_version_arn" in value:
        out["workflowBuildVersionArn"] = value["workflow_build_version_arn"]
    if "workflow_execution_id" in value:
        out["workflowExecutionId"] = value["workflow_execution_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "action" in value:
        out["action"] = value["action"]
    if "status" in value:
        import aws_sdk_imagebuilder.types.workflow_step_execution_status

        out["status"] = (
            aws_sdk_imagebuilder.types.workflow_step_execution_status.serialize_json(
                value["status"]
            )
        )
    if "rollback_status" in value:
        import aws_sdk_imagebuilder.types.workflow_step_execution_rollback_status

        out["rollbackStatus"] = (
            aws_sdk_imagebuilder.types.workflow_step_execution_rollback_status.serialize_json(
                value["rollback_status"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "inputs" in value:
        out["inputs"] = value["inputs"]
    if "outputs" in value:
        out["outputs"] = value["outputs"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "on_failure" in value:
        out["onFailure"] = value["on_failure"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    return out


def deserialize_json(data: dict) -> GetWorkflowStepExecutionResponse:
    out: GetWorkflowStepExecutionResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "stepExecutionId" in data:
        out["step_execution_id"] = data["stepExecutionId"]
    if "workflowBuildVersionArn" in data:
        out["workflow_build_version_arn"] = data["workflowBuildVersionArn"]
    if "workflowExecutionId" in data:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "action" in data:
        out["action"] = data["action"]
    if "status" in data:
        import aws_sdk_imagebuilder.types.workflow_step_execution_status

        out["status"] = (
            aws_sdk_imagebuilder.types.workflow_step_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "rollbackStatus" in data:
        import aws_sdk_imagebuilder.types.workflow_step_execution_rollback_status

        out["rollback_status"] = (
            aws_sdk_imagebuilder.types.workflow_step_execution_rollback_status.deserialize_json(
                data["rollbackStatus"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "inputs" in data:
        out["inputs"] = data["inputs"]
    if "outputs" in data:
        out["outputs"] = data["outputs"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    if "onFailure" in data:
        out["on_failure"] = data["onFailure"]
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    return out
