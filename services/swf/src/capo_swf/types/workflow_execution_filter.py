"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.workflow_id


class WorkflowExecutionFilter(TypedDict, closed=True):
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId to pass of match the criteria of this filter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionFilter) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionFilter:
    out: WorkflowExecutionFilter = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("WorkflowExecutionFilter.workflow_id required")
    return out
