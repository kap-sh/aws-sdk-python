"""Generated from Smithy shape ``com.amazonaws.ssm#CreateMaintenanceWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_id


class CreateMaintenanceWindowResult(TypedDict, closed=True):
    window_id: NotRequired["capo_ssm.types.maintenance_window_id.MaintenanceWindowId"]
    """<p>The ID of the created maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMaintenanceWindowResult:
    out: CreateMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    return out
