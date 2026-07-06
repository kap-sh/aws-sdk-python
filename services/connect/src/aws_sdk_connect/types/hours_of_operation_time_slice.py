"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationTimeSlice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours24_format
    import aws_sdk_connect.types.minutes_limit60


class HoursOfOperationTimeSlice(TypedDict, closed=True):
    hours: "aws_sdk_connect.types.hours24_format.Hours24Format"
    """<p>The hours.</p>"""
    minutes: "aws_sdk_connect.types.minutes_limit60.MinutesLimit60"
    """<p>The minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationTimeSlice) -> dict:
    out: dict = {}
    out["Hours"] = value["hours"]
    out["Minutes"] = value["minutes"]
    return out


def deserialize_json(data: dict) -> HoursOfOperationTimeSlice:
    out: HoursOfOperationTimeSlice = {}  # type: ignore[typeddict-item]
    if "Hours" in data:
        out["hours"] = data["Hours"]
    else:
        raise DeserializationError("HoursOfOperationTimeSlice.hours required")
    if "Minutes" in data:
        out["minutes"] = data["Minutes"]
    else:
        raise DeserializationError("HoursOfOperationTimeSlice.minutes required")
    return out
