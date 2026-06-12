"""Generated from Smithy shape ``com.amazonaws.datasync#TaskScheduleDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.schedule_disabled_by
    import aws_sdk_datasync.types.schedule_disabled_reason
    import aws_sdk_datasync.types.time


class TaskScheduleDetails(TypedDict):
    status_update_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>Indicates the last time the status of your task schedule changed. For example, if DataSync automatically disables your schedule because of a repeated error, you can see when the schedule was disabled.</p>"""
    disabled_reason: NotRequired[
        "aws_sdk_datasync.types.schedule_disabled_reason.ScheduleDisabledReason"
    ]
    """<p>Provides a reason if the task schedule is disabled.</p> <p>If your schedule is disabled by <code>USER</code>, you see a <code>Manually disabled by user.</code> message.</p> <p>If your schedule is disabled by <code>SERVICE</code>, you see an error message to help you understand why the task keeps failing. For information on resolving DataSync errors, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html\">Troubleshooting issues with DataSync transfers</a>.</p>"""
    disabled_by: NotRequired[
        "aws_sdk_datasync.types.schedule_disabled_by.ScheduleDisabledBy"
    ]
    """<p>Indicates how your task schedule was disabled.</p> <ul> <li> <p> <code>USER</code> - Your schedule was manually disabled by using the <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html\">UpdateTask</a> operation or DataSync console.</p> </li> <li> <p> <code>SERVICE</code> - Your schedule was automatically disabled by DataSync because the task failed repeatedly with the same error.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskScheduleDetails) -> dict:
    out: dict = {}
    if "status_update_time" in value:
        import aws_sdk_datasync.types.time

        out["StatusUpdateTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["status_update_time"]
        )
    if "disabled_reason" in value:
        out["DisabledReason"] = value["disabled_reason"]
    if "disabled_by" in value:
        import aws_sdk_datasync.types.schedule_disabled_by

        out["DisabledBy"] = (
            aws_sdk_datasync.types.schedule_disabled_by.serialize_aws_json_1_1(
                value["disabled_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskScheduleDetails:
    out: TaskScheduleDetails = {}  # type: ignore[typeddict-item]
    if "StatusUpdateTime" in data:
        import aws_sdk_datasync.types.time

        out["status_update_time"] = (
            aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
                data["StatusUpdateTime"]
            )
        )
    if "DisabledReason" in data:
        out["disabled_reason"] = data["DisabledReason"]
    if "DisabledBy" in data:
        import aws_sdk_datasync.types.schedule_disabled_by

        out["disabled_by"] = (
            aws_sdk_datasync.types.schedule_disabled_by.deserialize_aws_json_1_1(
                data["DisabledBy"]
            )
        )
    return out
