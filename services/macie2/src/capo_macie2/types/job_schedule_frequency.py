"""Generated from Smithy shape ``com.amazonaws.macie2#JobScheduleFrequency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.daily_schedule
    import capo_macie2.types.monthly_schedule
    import capo_macie2.types.weekly_schedule


class JobScheduleFrequency(TypedDict, closed=True):
    daily_schedule: NotRequired["capo_macie2.types.daily_schedule.DailySchedule"]
    """<p>Specifies a daily recurrence pattern for running the job.</p>"""
    monthly_schedule: NotRequired["capo_macie2.types.monthly_schedule.MonthlySchedule"]
    """<p>Specifies a monthly recurrence pattern for running the job.</p>"""
    weekly_schedule: NotRequired["capo_macie2.types.weekly_schedule.WeeklySchedule"]
    """<p>Specifies a weekly recurrence pattern for running the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobScheduleFrequency) -> dict:
    out: dict = {}
    if "daily_schedule" in value:
        import capo_macie2.types.daily_schedule

        out["dailySchedule"] = capo_macie2.types.daily_schedule.serialize_json(
            value["daily_schedule"]
        )
    if "monthly_schedule" in value:
        import capo_macie2.types.monthly_schedule

        out["monthlySchedule"] = capo_macie2.types.monthly_schedule.serialize_json(
            value["monthly_schedule"]
        )
    if "weekly_schedule" in value:
        import capo_macie2.types.weekly_schedule

        out["weeklySchedule"] = capo_macie2.types.weekly_schedule.serialize_json(
            value["weekly_schedule"]
        )
    return out


def deserialize_json(data: dict) -> JobScheduleFrequency:
    out: JobScheduleFrequency = {}  # type: ignore[typeddict-item]
    if "dailySchedule" in data:
        import capo_macie2.types.daily_schedule

        out["daily_schedule"] = capo_macie2.types.daily_schedule.deserialize_json(
            data["dailySchedule"]
        )
    if "monthlySchedule" in data:
        import capo_macie2.types.monthly_schedule

        out["monthly_schedule"] = capo_macie2.types.monthly_schedule.deserialize_json(
            data["monthlySchedule"]
        )
    if "weeklySchedule" in data:
        import capo_macie2.types.weekly_schedule

        out["weekly_schedule"] = capo_macie2.types.weekly_schedule.deserialize_json(
            data["weeklySchedule"]
        )
    return out
