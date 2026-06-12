"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowStepExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_step_execution_id


class GetWorkflowStepExecutionRequest(TypedDict):
    step_execution_id: (
        "aws_sdk_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    )
    """<p>Use the unique identifier for a specific runtime instance of the workflow step to get runtime details for that step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowStepExecutionRequest:
    out: GetWorkflowStepExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
