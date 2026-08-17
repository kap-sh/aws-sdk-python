"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterTargetFromMaintenanceWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_target_id


class DeregisterTargetFromMaintenanceWindowResult(TypedDict, closed=True):
    window_id: NotRequired["capo_ssm.types.maintenance_window_id.MaintenanceWindowId"]
    """<p>The ID of the maintenance window the target was removed from.</p>"""
    window_target_id: NotRequired[
        "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    ]
    """<p>The ID of the removed target definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTargetFromMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "window_target_id" in value:
        out["WindowTargetId"] = value["window_target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTargetFromMaintenanceWindowResult:
    out: DeregisterTargetFromMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    if data.get("WindowTargetId") is not None:
        out["window_target_id"] = data["WindowTargetId"]
    return out
