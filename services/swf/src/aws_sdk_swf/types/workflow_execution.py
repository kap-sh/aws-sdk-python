"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.workflow_id
    import aws_sdk_swf.types.workflow_run_id


class WorkflowExecution(TypedDict, closed=True):
    workflow_id: "aws_sdk_swf.types.workflow_id.WorkflowId"
    """<p>The user defined identifier associated with the workflow execution.</p>"""
    run_id: "aws_sdk_swf.types.workflow_run_id.WorkflowRunId"
    """<p>A system-generated unique identifier for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecution) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    out["runId"] = value["run_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecution:
    out: WorkflowExecution = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("WorkflowExecution.workflow_id required")
    if "runId" in data:
        out["run_id"] = data["runId"]
    else:
        raise DeserializationError("WorkflowExecution.run_id required")
    return out
