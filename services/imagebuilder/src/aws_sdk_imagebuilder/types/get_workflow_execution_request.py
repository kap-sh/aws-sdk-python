"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_execution_id


class GetWorkflowExecutionRequest(TypedDict, closed=True):
    workflow_execution_id: (
        "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    )
    """<p>Use the unique identifier for a runtime instance of the workflow to get runtime details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowExecutionRequest:
    out: GetWorkflowExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
