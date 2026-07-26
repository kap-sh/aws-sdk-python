"""Generated from Smithy shape ``com.amazonaws.inspector2#Time``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.time_of_day
    import capo_inspector2.types.timezone


class Time(TypedDict, closed=True):
    time_of_day: "capo_inspector2.types.time_of_day.TimeOfDay"
    """<p>The time of day in 24-hour format (00:00).</p>"""
    timezone: "capo_inspector2.types.timezone.Timezone"
    """<p>The timezone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Time) -> dict:
    out: dict = {}
    out["timeOfDay"] = value["time_of_day"]
    out["timezone"] = value["timezone"]
    return out


def deserialize_json(data: dict) -> Time:
    out: Time = {}  # type: ignore[typeddict-item]
    if "timeOfDay" in data:
        out["time_of_day"] = data["timeOfDay"]
    else:
        raise DeserializationError("Time.time_of_day required")
    if "timezone" in data:
        out["timezone"] = data["timezone"]
    else:
        raise DeserializationError("Time.timezone required")
    return out
