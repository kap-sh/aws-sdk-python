"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.workflow_build_version_arn
    import capo_imagebuilder.types.workflow_execution_id
    import capo_imagebuilder.types.workflow_step_action
    import capo_imagebuilder.types.workflow_step_execution_id
    import capo_imagebuilder.types.workflow_step_name


class WorkflowStepExecution(TypedDict, closed=True):
    step_execution_id: NotRequired[
        "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    ]
    """<p>Uniquely identifies the workflow step that ran for the associated image build version.</p>"""
    image_build_version_arn: NotRequired[
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image build version that ran the workflow.</p>"""
    workflow_execution_id: NotRequired[
        "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    ]
    """<p>Uniquely identifies the runtime instance of the workflow that contains the workflow step that ran for the associated image build version.</p>"""
    workflow_build_version_arn: NotRequired[
        "capo_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource that ran.</p>"""
    name: NotRequired["capo_imagebuilder.types.workflow_step_name.WorkflowStepName"]
    """<p>The name of the workflow step.</p>"""
    action: NotRequired[
        "capo_imagebuilder.types.workflow_step_action.WorkflowStepAction"
    ]
    """<p>The name of the step action.</p>"""
    start_time: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the workflow step started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepExecution) -> dict:
    out: dict = {}
    if "step_execution_id" in value:
        out["stepExecutionId"] = value["step_execution_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "workflow_execution_id" in value:
        out["workflowExecutionId"] = value["workflow_execution_id"]
    if "workflow_build_version_arn" in value:
        out["workflowBuildVersionArn"] = value["workflow_build_version_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "action" in value:
        out["action"] = value["action"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    return out


def deserialize_json(data: dict) -> WorkflowStepExecution:
    out: WorkflowStepExecution = {}  # type: ignore[typeddict-item]
    if "stepExecutionId" in data:
        out["step_execution_id"] = data["stepExecutionId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "workflowExecutionId" in data:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    if "workflowBuildVersionArn" in data:
        out["workflow_build_version_arn"] = data["workflowBuildVersionArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "action" in data:
        out["action"] = data["action"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    return out
