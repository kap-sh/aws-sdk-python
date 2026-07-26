"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_task_id


class GetMaintenanceWindowExecutionTaskRequest(TypedDict, closed=True):
    window_execution_id: (
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution that includes the task.</p>"""
    task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    """<p>The ID of the specific task execution in the maintenance window task that should be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionTaskRequest) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionTaskRequest:
    out: GetMaintenanceWindowExecutionTaskRequest = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowExecutionTaskRequest.window_execution_id required"
        )
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowExecutionTaskRequest.task_id required"
        )
    return out
