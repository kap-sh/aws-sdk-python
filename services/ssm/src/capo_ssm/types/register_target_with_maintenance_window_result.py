"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterTargetWithMaintenanceWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_target_id


class RegisterTargetWithMaintenanceWindowResult(TypedDict, closed=True):
    window_target_id: NotRequired[
        "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    ]
    """<p>The ID of the target definition in this maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTargetWithMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_target_id" in value:
        out["WindowTargetId"] = value["window_target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTargetWithMaintenanceWindowResult:
    out: RegisterTargetWithMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowTargetId") is not None:
        out["window_target_id"] = data["WindowTargetId"]
    return out
