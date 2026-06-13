"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFrequency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.refresh_interval
    import aws_sdk_quicksight.types.schedule_refresh_on_entity
    import aws_sdk_quicksight.types.string


class RefreshFrequency(TypedDict):
    interval: "aws_sdk_quicksight.types.refresh_interval.RefreshInterval"
    """<p>The interval between scheduled refreshes. Valid values are as follows:</p> <ul> <li> <p> <code>MINUTE15</code>: The dataset refreshes every 15 minutes. This value is only supported for incremental refreshes. This interval can only be used for one schedule per dataset.</p> </li> <li> <p> <code>MINUTE30</code>:The dataset refreshes every 30 minutes. This value is only supported for incremental refreshes. This interval can only be used for one schedule per dataset.</p> </li> <li> <p> <code>HOURLY</code>: The dataset refreshes every hour. This interval can only be used for one schedule per dataset.</p> </li> <li> <p> <code>DAILY</code>: The dataset refreshes every day.</p> </li> <li> <p> <code>WEEKLY</code>: The dataset refreshes every week.</p> </li> <li> <p> <code>MONTHLY</code>: The dataset refreshes every month.</p> </li> </ul>"""
    refresh_on_day: NotRequired[
        "aws_sdk_quicksight.types.schedule_refresh_on_entity.ScheduleRefreshOnEntity"
    ]
    """<p>The day of the week that you want to schedule the refresh on. This value is required for weekly and monthly refresh intervals.</p>"""
    timezone: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The timezone that you want the refresh schedule to use. The timezone ID must match a corresponding ID found on <code>java.util.time.getAvailableIDs()</code>.</p>"""
    time_of_the_day: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The time of day that you want the datset to refresh. This value is expressed in HH:MM format. This field is not required for schedules that refresh hourly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshFrequency) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.refresh_interval

    out["Interval"] = aws_sdk_quicksight.types.refresh_interval.serialize_json(
        value["interval"]
    )
    if "refresh_on_day" in value:
        import aws_sdk_quicksight.types.schedule_refresh_on_entity

        out["RefreshOnDay"] = (
            aws_sdk_quicksight.types.schedule_refresh_on_entity.serialize_json(
                value["refresh_on_day"]
            )
        )
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "time_of_the_day" in value:
        out["TimeOfTheDay"] = value["time_of_the_day"]
    return out


def deserialize_json(data: dict) -> RefreshFrequency:
    out: RefreshFrequency = {}  # type: ignore[typeddict-item]
    if "Interval" in data:
        import aws_sdk_quicksight.types.refresh_interval

        out["interval"] = aws_sdk_quicksight.types.refresh_interval.deserialize_json(
            data["Interval"]
        )
    else:
        raise DeserializationError("RefreshFrequency.interval required")
    if "RefreshOnDay" in data:
        import aws_sdk_quicksight.types.schedule_refresh_on_entity

        out["refresh_on_day"] = (
            aws_sdk_quicksight.types.schedule_refresh_on_entity.deserialize_json(
                data["RefreshOnDay"]
            )
        )
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "TimeOfTheDay" in data:
        out["time_of_the_day"] = data["TimeOfTheDay"]
    return out
