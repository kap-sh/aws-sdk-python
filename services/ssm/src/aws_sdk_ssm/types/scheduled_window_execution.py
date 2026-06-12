"""Generated from Smithy shape ``com.amazonaws.ssm#ScheduledWindowExecution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_string_date_time


class ScheduledWindowExecution(TypedDict):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the maintenance window to be run.</p>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The name of the maintenance window to be run.</p>"""
    execution_time: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The time, in ISO-8601 Extended format, that the maintenance window is scheduled to be run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledWindowExecution) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "execution_time" in value:
        out["ExecutionTime"] = value["execution_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledWindowExecution:
    out: ScheduledWindowExecution = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ExecutionTime" in data:
        out["execution_time"] = data["ExecutionTime"]
    return out
