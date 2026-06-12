"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RefreshSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.refresh_schedule_frequency
    import aws_sdk_cloudtrail.types.refresh_schedule_status
    import aws_sdk_cloudtrail.types.time_of_day


class RefreshSchedule(TypedDict):
    frequency: NotRequired[
        "aws_sdk_cloudtrail.types.refresh_schedule_frequency.RefreshScheduleFrequency"
    ]
    """<p> The frequency at which you want the dashboard refreshed. </p>"""
    status: NotRequired[
        "aws_sdk_cloudtrail.types.refresh_schedule_status.RefreshScheduleStatus"
    ]
    """<p> Specifies whether the refresh schedule is enabled. Set the value to <code>ENABLED</code> to enable the refresh schedule, or to <code>DISABLED</code> to turn off the refresh schedule. </p>"""
    time_of_day: NotRequired["aws_sdk_cloudtrail.types.time_of_day.TimeOfDay"]
    """<p> The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshSchedule) -> dict:
    out: dict = {}
    if "frequency" in value:
        import aws_sdk_cloudtrail.types.refresh_schedule_frequency

        out["Frequency"] = (
            aws_sdk_cloudtrail.types.refresh_schedule_frequency.serialize_aws_json_1_1(
                value["frequency"]
            )
        )
    if "status" in value:
        import aws_sdk_cloudtrail.types.refresh_schedule_status

        out["Status"] = (
            aws_sdk_cloudtrail.types.refresh_schedule_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "time_of_day" in value:
        out["TimeOfDay"] = value["time_of_day"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshSchedule:
    out: RefreshSchedule = {}  # type: ignore[typeddict-item]
    if "Frequency" in data:
        import aws_sdk_cloudtrail.types.refresh_schedule_frequency

        out["frequency"] = (
            aws_sdk_cloudtrail.types.refresh_schedule_frequency.deserialize_aws_json_1_1(
                data["Frequency"]
            )
        )
    if "Status" in data:
        import aws_sdk_cloudtrail.types.refresh_schedule_status

        out["status"] = (
            aws_sdk_cloudtrail.types.refresh_schedule_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "TimeOfDay" in data:
        out["time_of_day"] = data["TimeOfDay"]
    return out
