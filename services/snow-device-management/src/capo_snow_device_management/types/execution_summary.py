"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.execution_id
    import capo_snow_device_management.types.execution_state
    import capo_snow_device_management.types.managed_device_id
    import capo_snow_device_management.types.task_id


class ExecutionSummary(TypedDict, closed=True):
    task_id: NotRequired["capo_snow_device_management.types.task_id.TaskId"]
    """<p>The ID of the task.</p>"""
    execution_id: NotRequired[
        "capo_snow_device_management.types.execution_id.ExecutionId"
    ]
    """<p>The ID of the execution.</p>"""
    managed_device_id: NotRequired[
        "capo_snow_device_management.types.managed_device_id.ManagedDeviceId"
    ]
    """<p>The ID of the managed device that the task is being executed on.</p>"""
    state: NotRequired[
        "capo_snow_device_management.types.execution_state.ExecutionState"
    ]
    """<p>The state of the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummary) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "managed_device_id" in value:
        out["managedDeviceId"] = value["managed_device_id"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> ExecutionSummary:
    out: ExecutionSummary = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "managedDeviceId" in data:
        out["managed_device_id"] = data["managedDeviceId"]
    if "state" in data:
        out["state"] = data["state"]
    return out
