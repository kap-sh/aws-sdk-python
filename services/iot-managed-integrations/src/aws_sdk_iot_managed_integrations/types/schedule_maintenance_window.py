"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ScheduleMaintenanceWindow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.duration_in_minutes
    import aws_sdk_iot_managed_integrations.types.start_time


class ScheduleMaintenanceWindow(TypedDict):
    duration_in_minutes: NotRequired[
        "aws_sdk_iot_managed_integrations.types.duration_in_minutes.DurationInMinutes"
    ]
    """<p>Displays the duration of the next maintenance window.</p>"""
    start_time: NotRequired[
        "aws_sdk_iot_managed_integrations.types.start_time.StartTime"
    ]
    """<p>Displays the start time of the next maintenance window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleMaintenanceWindow) -> dict:
    out: dict = {}
    if "duration_in_minutes" in value:
        out["DurationInMinutes"] = value["duration_in_minutes"]
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    return out


def deserialize_json(data: dict) -> ScheduleMaintenanceWindow:
    out: ScheduleMaintenanceWindow = {}  # type: ignore[typeddict-item]
    if "DurationInMinutes" in data:
        out["duration_in_minutes"] = data["DurationInMinutes"]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    return out
