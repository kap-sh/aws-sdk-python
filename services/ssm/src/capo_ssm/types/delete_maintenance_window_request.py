"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_id


class DeleteMaintenanceWindowRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMaintenanceWindowRequest:
    out: DeleteMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError("DeleteMaintenanceWindowRequest.window_id required")
    return out
