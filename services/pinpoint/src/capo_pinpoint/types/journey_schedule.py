"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.__timestamp_iso8601


class JourneySchedule(TypedDict, closed=True):
    end_time: NotRequired["capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The scheduled time, in ISO 8601 format, when the journey ended or will end.</p>"""
    start_time: NotRequired[
        "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The scheduled time, in ISO 8601 format, when the journey began or will begin.</p>"""
    timezone: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The starting UTC offset for the journey schedule, if the value of the journey's LocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+08:45, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+12:45, UTC+13, UTC+13:45, UTC-02, UTC-02:30, UTC-03, UTC-03:30, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-09:30, UTC-10, and UTC-11.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneySchedule) -> dict:
    out: dict = {}
    if "end_time" in value:
        import capo_pinpoint.types.__timestamp_iso8601

        out["EndTime"] = capo_pinpoint.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    if "start_time" in value:
        import capo_pinpoint.types.__timestamp_iso8601

        out["StartTime"] = capo_pinpoint.types.__timestamp_iso8601.serialize_json(
            value["start_time"]
        )
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_json(data: dict) -> JourneySchedule:
    out: JourneySchedule = {}  # type: ignore[typeddict-item]
    if "EndTime" in data:
        import capo_pinpoint.types.__timestamp_iso8601

        out["end_time"] = capo_pinpoint.types.__timestamp_iso8601.deserialize_json(
            data["EndTime"]
        )
    if "StartTime" in data:
        import capo_pinpoint.types.__timestamp_iso8601

        out["start_time"] = capo_pinpoint.types.__timestamp_iso8601.deserialize_json(
            data["StartTime"]
        )
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    return out
