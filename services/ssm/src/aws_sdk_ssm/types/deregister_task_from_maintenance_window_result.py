"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterTaskFromMaintenanceWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_task_id


class DeregisterTaskFromMaintenanceWindowResult(TypedDict, closed=True):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the maintenance window the task was removed from.</p>"""
    window_task_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    ]
    """<p>The ID of the task removed from the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTaskFromMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "window_task_id" in value:
        out["WindowTaskId"] = value["window_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTaskFromMaintenanceWindowResult:
    out: DeregisterTaskFromMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    if "WindowTaskId" in data:
        out["window_task_id"] = data["WindowTaskId"]
    return out
