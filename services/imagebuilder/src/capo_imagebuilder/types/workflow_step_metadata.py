"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.workflow_step_action
    import capo_imagebuilder.types.workflow_step_description
    import capo_imagebuilder.types.workflow_step_execution_id
    import capo_imagebuilder.types.workflow_step_execution_rollback_status
    import capo_imagebuilder.types.workflow_step_execution_status
    import capo_imagebuilder.types.workflow_step_inputs
    import capo_imagebuilder.types.workflow_step_message
    import capo_imagebuilder.types.workflow_step_name
    import capo_imagebuilder.types.workflow_step_outputs


class WorkflowStepMetadata(TypedDict, closed=True):
    step_execution_id: NotRequired[
        "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    ]
    """<p>A unique identifier for the workflow step, assigned at runtime.</p>"""
    name: NotRequired["capo_imagebuilder.types.workflow_step_name.WorkflowStepName"]
    """<p>The name of the workflow step.</p>"""
    description: NotRequired[
        "capo_imagebuilder.types.workflow_step_description.WorkflowStepDescription"
    ]
    """<p>Description of the workflow step.</p>"""
    action: NotRequired[
        "capo_imagebuilder.types.workflow_step_action.WorkflowStepAction"
    ]
    """<p>The step action name.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.workflow_step_execution_status.WorkflowStepExecutionStatus"
    ]
    """<p>Runtime status for the workflow step.</p>"""
    rollback_status: NotRequired[
        "capo_imagebuilder.types.workflow_step_execution_rollback_status.WorkflowStepExecutionRollbackStatus"
    ]
    """<p>Reports on the rollback status of the step, if applicable.</p>"""
    message: NotRequired[
        "capo_imagebuilder.types.workflow_step_message.WorkflowStepMessage"
    ]
    """<p>Detailed output message that the workflow step provides at runtime.</p>"""
    inputs: NotRequired[
        "capo_imagebuilder.types.workflow_step_inputs.WorkflowStepInputs"
    ]
    """<p>Input parameters that Image Builder provides for the workflow step.</p>"""
    outputs: NotRequired[
        "capo_imagebuilder.types.workflow_step_outputs.WorkflowStepOutputs"
    ]
    """<p>The file names that the workflow step created as output for this runtime instance of the workflow.</p>"""
    start_time: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the workflow step started.</p>"""
    end_time: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the workflow step finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepMetadata) -> dict:
    out: dict = {}
    if "step_execution_id" in value:
        out["stepExecutionId"] = value["step_execution_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "action" in value:
        out["action"] = value["action"]
    if "status" in value:
        import capo_imagebuilder.types.workflow_step_execution_status

        out["status"] = (
            capo_imagebuilder.types.workflow_step_execution_status.serialize_json(
                value["status"]
            )
        )
    if "rollback_status" in value:
        import capo_imagebuilder.types.workflow_step_execution_rollback_status

        out["rollbackStatus"] = (
            capo_imagebuilder.types.workflow_step_execution_rollback_status.serialize_json(
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
    return out


def deserialize_json(data: dict) -> WorkflowStepMetadata:
    out: WorkflowStepMetadata = {}  # type: ignore[typeddict-item]
    if "stepExecutionId" in data:
        out["step_execution_id"] = data["stepExecutionId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "action" in data:
        out["action"] = data["action"]
    if "status" in data:
        import capo_imagebuilder.types.workflow_step_execution_status

        out["status"] = (
            capo_imagebuilder.types.workflow_step_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "rollbackStatus" in data:
        import capo_imagebuilder.types.workflow_step_execution_rollback_status

        out["rollback_status"] = (
            capo_imagebuilder.types.workflow_step_execution_rollback_status.deserialize_json(
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
    return out
