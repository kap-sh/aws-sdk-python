"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterTargetFromMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_target_id


class DeregisterTargetFromMaintenanceWindowRequest(TypedDict):
    window_id: "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window the target should be removed from.</p>"""
    window_target_id: (
        "aws_sdk_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    )
    """<p>The ID of the target definition to remove.</p>"""
    safe: NotRequired["aws_sdk_ssm.types.boolean.Boolean"]
    """<p>The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and doesn't deregister the target from the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTargetFromMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTargetId"] = value["window_target_id"]
    if "safe" in value:
        out["Safe"] = value["safe"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeregisterTargetFromMaintenanceWindowRequest:
    out: DeregisterTargetFromMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "DeregisterTargetFromMaintenanceWindowRequest.window_id required"
        )
    if "WindowTargetId" in data:
        out["window_target_id"] = data["WindowTargetId"]
    else:
        raise DeserializationError(
            "DeregisterTargetFromMaintenanceWindowRequest.window_target_id required"
        )
    if "Safe" in data:
        out["safe"] = data["Safe"]
    return out
