"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteMaintenanceWindowResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_id


class DeleteMaintenanceWindowResult(TypedDict):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the deleted maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMaintenanceWindowResult) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMaintenanceWindowResult:
    out: DeleteMaintenanceWindowResult = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    return out
