"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CalendarInterval``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.calendar_interval_duration
    import aws_sdk_application_signals.types.duration_unit


class CalendarInterval(TypedDict):
    start_time: "datetime.datetime"
    """<p>The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.</p> <p>When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>As soon as one calendar interval ends, another automatically begins.</p>"""
    duration_unit: "aws_sdk_application_signals.types.duration_unit.DurationUnit"
    """<p>Specifies the calendar interval unit.</p>"""
    duration: "aws_sdk_application_signals.types.calendar_interval_duration.CalendarIntervalDuration"
    """<p>Specifies the duration of each calendar interval. For example, if <code>Duration</code> is <code>1</code> and <code>DurationUnit</code> is <code>MONTH</code>, each interval is one month, aligned with the calendar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalendarInterval) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types._prelude.timestamp

    out["StartTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import aws_sdk_application_signals.types.duration_unit

    out["DurationUnit"] = (
        aws_sdk_application_signals.types.duration_unit.serialize_json(
            value["duration_unit"]
        )
    )
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> CalendarInterval:
    out: CalendarInterval = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("CalendarInterval.start_time required")
    if "DurationUnit" in data:
        import aws_sdk_application_signals.types.duration_unit

        out["duration_unit"] = (
            aws_sdk_application_signals.types.duration_unit.deserialize_json(
                data["DurationUnit"]
            )
        )
    else:
        raise DeserializationError("CalendarInterval.duration_unit required")
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("CalendarInterval.duration required")
    return out
