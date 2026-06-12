"""Generated from Smithy shape ``com.amazonaws.customerprofiles#JobSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.job_schedule_day_of_the_week
    import aws_sdk_customer_profiles.types.job_schedule_time


class JobSchedule(TypedDict):
    day_of_the_week: "aws_sdk_customer_profiles.types.job_schedule_day_of_the_week.JobScheduleDayOfTheWeek"
    """<p>The day when the Identity Resolution Job should run every week.</p>"""
    time: "aws_sdk_customer_profiles.types.job_schedule_time.JobScheduleTime"
    """<p>The time when the Identity Resolution Job should run every week.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSchedule) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.job_schedule_day_of_the_week

    out["DayOfTheWeek"] = (
        aws_sdk_customer_profiles.types.job_schedule_day_of_the_week.serialize_json(
            value["day_of_the_week"]
        )
    )
    out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> JobSchedule:
    out: JobSchedule = {}  # type: ignore[typeddict-item]
    if "DayOfTheWeek" in data:
        import aws_sdk_customer_profiles.types.job_schedule_day_of_the_week

        out["day_of_the_week"] = (
            aws_sdk_customer_profiles.types.job_schedule_day_of_the_week.deserialize_json(
                data["DayOfTheWeek"]
            )
        )
    else:
        raise DeserializationError("JobSchedule.day_of_the_week required")
    if "Time" in data:
        out["time"] = data["Time"]
    else:
        raise DeserializationError("JobSchedule.time required")
    return out
