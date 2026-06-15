"""Generated from Smithy shape ``com.amazonaws.ssm#CreateMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.client_token
    import aws_sdk_ssm.types.maintenance_window_allow_unassociated_targets
    import aws_sdk_ssm.types.maintenance_window_cutoff
    import aws_sdk_ssm.types.maintenance_window_description
    import aws_sdk_ssm.types.maintenance_window_duration_hours
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_offset
    import aws_sdk_ssm.types.maintenance_window_schedule
    import aws_sdk_ssm.types.maintenance_window_string_date_time
    import aws_sdk_ssm.types.maintenance_window_timezone
    import aws_sdk_ssm.types.tag_list


class CreateMaintenanceWindowRequest(TypedDict):
    name: "aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"
    """<p>The name of the maintenance window.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>An optional description for the maintenance window. We recommend specifying a description to help you organize your maintenance windows. </p>"""
    start_date: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. <code>StartDate</code> allows you to delay activation of the maintenance window until the specified future date.</p> <note> <p>When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date. </p> </note>"""
    end_date: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
    ]
    """<p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. <code>EndDate</code> allows you to set a date and time in the future when the maintenance window will no longer run.</p>"""
    schedule: "aws_sdk_ssm.types.maintenance_window_schedule.MaintenanceWindowSchedule"
    """<p>The schedule of the maintenance window in the form of a cron or rate expression.</p>"""
    schedule_timezone: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_timezone.MaintenanceWindowTimezone"
    ]
    r"""<p>The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"UTC\", or \"Asia/Seoul\". For more information, see the <a href=\"https://www.iana.org/time-zones\">Time Zone Database</a> on the IANA website.</p>"""
    schedule_offset: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_offset.MaintenanceWindowOffset"
    ]
    """<p>The number of days to wait after the date and time specified by a cron expression before running the maintenance window.</p> <p>For example, the following cron expression schedules a maintenance window to run on the third Tuesday of every month at 11:30 PM.</p> <p> <code>cron(30 23 ? * TUE#3 *)</code> </p> <p>If the schedule offset is <code>2</code>, the maintenance window won't run until two days later.</p>"""
    duration: "aws_sdk_ssm.types.maintenance_window_duration_hours.MaintenanceWindowDurationHours"
    """<p>The duration of the maintenance window in hours.</p>"""
    cutoff: "aws_sdk_ssm.types.maintenance_window_cutoff.MaintenanceWindowCutoff"
    """<p>The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.</p>"""
    allow_unassociated_targets: "aws_sdk_ssm.types.maintenance_window_allow_unassociated_targets.MaintenanceWindowAllowUnassociatedTargets"
    """<p>Enables a maintenance window task to run on managed nodes, even if you haven't registered those nodes as targets. If enabled, then you must specify the unregistered managed nodes (by node ID) when you register a task with the maintenance window.</p> <p>If you don't enable this option, then you must specify previously-registered targets when you register a task with the maintenance window.</p>"""
    client_token: NotRequired["aws_sdk_ssm.types.client_token.ClientToken"]
    """<p>User-provided idempotency token.</p>"""
    tags: NotRequired["aws_sdk_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=TaskType,Value=AgentUpdate</code> </p> </li> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> </ul> <note> <p>To add tags to an existing maintenance window, use the <a>AddTagsToResource</a> operation.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    out["Schedule"] = value["schedule"]
    if "schedule_timezone" in value:
        out["ScheduleTimezone"] = value["schedule_timezone"]
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    out["Duration"] = value["duration"]
    out["Cutoff"] = value.get("cutoff", 0)
    out["AllowUnassociatedTargets"] = value.get("allow_unassociated_targets", False)
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_ssm.types.tag_list

        out["Tags"] = aws_sdk_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMaintenanceWindowRequest:
    out: CreateMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateMaintenanceWindowRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "StartDate" in data:
        out["start_date"] = data["StartDate"]
    if "EndDate" in data:
        out["end_date"] = data["EndDate"]
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    else:
        raise DeserializationError("CreateMaintenanceWindowRequest.schedule required")
    if "ScheduleTimezone" in data:
        out["schedule_timezone"] = data["ScheduleTimezone"]
    if "ScheduleOffset" in data:
        out["schedule_offset"] = data["ScheduleOffset"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("CreateMaintenanceWindowRequest.duration required")
    if "Cutoff" in data:
        out["cutoff"] = data["Cutoff"]
    else:
        out["cutoff"] = 0
    if "AllowUnassociatedTargets" in data:
        out["allow_unassociated_targets"] = data["AllowUnassociatedTargets"]
    else:
        out["allow_unassociated_targets"] = False
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_ssm.types.tag_list

        out["tags"] = aws_sdk_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
