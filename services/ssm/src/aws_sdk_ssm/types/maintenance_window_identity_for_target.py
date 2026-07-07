"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowIdentityForTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name


class MaintenanceWindowIdentityForTarget(TypedDict, closed=True):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the maintenance window.</p>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The name of the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowIdentityForTarget) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowIdentityForTarget:
    out: MaintenanceWindowIdentityForTarget = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
