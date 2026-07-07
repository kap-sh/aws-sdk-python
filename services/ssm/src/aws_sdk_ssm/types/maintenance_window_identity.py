"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_cutoff
    import aws_sdk_ssm.types.maintenance_window_description
    import aws_sdk_ssm.types.maintenance_window_duration_hours
    import aws_sdk_ssm.types.maintenance_window_enabled
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_offset
    import aws_sdk_ssm.types.maintenance_window_schedule
    import aws_sdk_ssm.types.maintenance_window_string_date_time
    import aws_sdk_ssm.types.maintenance_window_timezone


class MaintenanceWindowIdentity(TypedDict, closed=True):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the maintenance window.</p>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The name of the maintenance window.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>A description of the maintenance window.</p>"""
    enabled: "aws_sdk_ssm.types.maintenance_window_enabled.MaintenanceWindowEnabled"
    """<p>Indicates whether the maintenance window is enabled.</p>"""
    duration: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_duration_hours.MaintenanceWindowDurationHours"
    ]
    """<p>The duration of the maintenance window in hours.</p>"""
    cutoff: "aws_sdk_ssm.types.maintenance_window_cutoff.MaintenanceWindowCutoff"
    """<p>The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.</p>"""
    schedule: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_schedule.MaintenanceWindowSchedule"
    ]
    """<p>The schedule of the maintenance window in the form of a cron or rate expression.</p>"""
    schedule_timezone: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_timezone.MaintenanceWindowTimezone"
    ]
    """<p>The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.</p>"""
    schedule_offset: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_offset.MaintenanceWindowOffset"
    ]
    """<p>The number of days to wait to run a maintenance window after the scheduled cron expression date and time.</p>"""
    end_date: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.</p>"""
    start_date: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.</p>"""
    next_execution_time: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowIdentity) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Enabled"] = value.get("enabled", False)
    if "duration" in value:
        out["Duration"] = value["duration"]
    out["Cutoff"] = value.get("cutoff", 0)
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "schedule_timezone" in value:
        out["ScheduleTimezone"] = value["schedule_timezone"]
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "next_execution_time" in value:
        out["NextExecutionTime"] = value["next_execution_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowIdentity:
    out: MaintenanceWindowIdentity = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "Cutoff" in data:
        out["cutoff"] = data["Cutoff"]
    else:
        out["cutoff"] = 0
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    if "ScheduleTimezone" in data:
        out["schedule_timezone"] = data["ScheduleTimezone"]
    if "ScheduleOffset" in data:
        out["schedule_offset"] = data["ScheduleOffset"]
    if "EndDate" in data:
        out["end_date"] = data["EndDate"]
    if "StartDate" in data:
        out["start_date"] = data["StartDate"]
    if "NextExecutionTime" in data:
        out["next_execution_time"] = data["NextExecutionTime"]
    return out
