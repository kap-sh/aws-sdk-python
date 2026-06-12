"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_task_id


class GetMaintenanceWindowTaskRequest(TypedDict):
    window_id: "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The maintenance window ID that includes the task to retrieve.</p>"""
    window_task_id: (
        "aws_sdk_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    )
    """<p>The maintenance window task ID to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowTaskRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTaskId"] = value["window_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowTaskRequest:
    out: GetMaintenanceWindowTaskRequest = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError("GetMaintenanceWindowTaskRequest.window_id required")
    if "WindowTaskId" in data:
        out["window_task_id"] = data["WindowTaskId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowTaskRequest.window_task_id required"
        )
    return out
