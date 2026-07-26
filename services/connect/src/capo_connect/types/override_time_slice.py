"""Generated from Smithy shape ``com.amazonaws.connect#OverrideTimeSlice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hours24_format
    import capo_connect.types.minutes_limit60


class OverrideTimeSlice(TypedDict, closed=True):
    hours: "capo_connect.types.hours24_format.Hours24Format"
    """<p>The hours.</p>"""
    minutes: "capo_connect.types.minutes_limit60.MinutesLimit60"
    """<p>The minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideTimeSlice) -> dict:
    out: dict = {}
    out["Hours"] = value["hours"]
    out["Minutes"] = value["minutes"]
    return out


def deserialize_json(data: dict) -> OverrideTimeSlice:
    out: OverrideTimeSlice = {}  # type: ignore[typeddict-item]
    if "Hours" in data:
        out["hours"] = data["Hours"]
    else:
        raise DeserializationError("OverrideTimeSlice.hours required")
    if "Minutes" in data:
        out["minutes"] = data["Minutes"]
    else:
        raise DeserializationError("OverrideTimeSlice.minutes required")
    return out
