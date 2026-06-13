"""Generated from Smithy shape ``com.amazonaws.inspector2#Schedule``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.daily_schedule
    import aws_sdk_inspector2.types.monthly_schedule
    import aws_sdk_inspector2.types.one_time_schedule
    import aws_sdk_inspector2.types.weekly_schedule


class _Schedule_oneTime(TypedDict):
    oneTime: "aws_sdk_inspector2.types.one_time_schedule.OneTimeSchedule"


class _Schedule_daily(TypedDict):
    daily: "aws_sdk_inspector2.types.daily_schedule.DailySchedule"


class _Schedule_weekly(TypedDict):
    weekly: "aws_sdk_inspector2.types.weekly_schedule.WeeklySchedule"


class _Schedule_monthly(TypedDict):
    monthly: "aws_sdk_inspector2.types.monthly_schedule.MonthlySchedule"


Schedule: TypeAlias = (
    _Schedule_oneTime | _Schedule_daily | _Schedule_weekly | _Schedule_monthly
)


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    if "oneTime" in value:
        import aws_sdk_inspector2.types.one_time_schedule

        return {
            "oneTime": aws_sdk_inspector2.types.one_time_schedule.serialize_json(
                value["oneTime"]
            )
        }
    elif "daily" in value:
        import aws_sdk_inspector2.types.daily_schedule

        return {
            "daily": aws_sdk_inspector2.types.daily_schedule.serialize_json(
                value["daily"]
            )
        }
    elif "weekly" in value:
        import aws_sdk_inspector2.types.weekly_schedule

        return {
            "weekly": aws_sdk_inspector2.types.weekly_schedule.serialize_json(
                value["weekly"]
            )
        }
    elif "monthly" in value:
        import aws_sdk_inspector2.types.monthly_schedule

        return {
            "monthly": aws_sdk_inspector2.types.monthly_schedule.serialize_json(
                value["monthly"]
            )
        }
    else:
        raise SerializationError("Schedule: no variant present")


def deserialize_json(data: dict) -> Schedule:
    if "oneTime" in data:
        import aws_sdk_inspector2.types.one_time_schedule

        return {
            "oneTime": aws_sdk_inspector2.types.one_time_schedule.deserialize_json(
                data["oneTime"]
            )
        }
    elif "daily" in data:
        import aws_sdk_inspector2.types.daily_schedule

        return {
            "daily": aws_sdk_inspector2.types.daily_schedule.deserialize_json(
                data["daily"]
            )
        }
    elif "weekly" in data:
        import aws_sdk_inspector2.types.weekly_schedule

        return {
            "weekly": aws_sdk_inspector2.types.weekly_schedule.deserialize_json(
                data["weekly"]
            )
        }
    elif "monthly" in data:
        import aws_sdk_inspector2.types.monthly_schedule

        return {
            "monthly": aws_sdk_inspector2.types.monthly_schedule.deserialize_json(
                data["monthly"]
            )
        }
    else:
        raise DeserializationError("Schedule: no recognized variant key")
