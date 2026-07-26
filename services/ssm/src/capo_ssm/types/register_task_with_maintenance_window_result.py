"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterTaskWithMaintenanceWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task_id


class RegisterTaskWithMaintenanceWindowResult(TypedDict, closed=True):
    window_task_id: NotRequired[
        "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    ]
    """<p>The ID of the task in the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTaskWithMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_task_id" in value:
        out["WindowTaskId"] = value["window_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTaskWithMaintenanceWindowResult:
    out: RegisterTaskWithMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if "WindowTaskId" in data:
        out["window_task_id"] = data["WindowTaskId"]
    return out
