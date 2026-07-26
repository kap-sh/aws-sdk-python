"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyTimeframeCap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer


class JourneyTimeframeCap(TypedDict, closed=True):
    cap: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply.</p>"""
    days: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyTimeframeCap) -> dict:
    out: dict = {}
    if "cap" in value:
        out["Cap"] = value["cap"]
    if "days" in value:
        out["Days"] = value["days"]
    return out


def deserialize_json(data: dict) -> JourneyTimeframeCap:
    out: JourneyTimeframeCap = {}  # type: ignore[typeddict-item]
    if "Cap" in data:
        out["cap"] = data["Cap"]
    if "Days" in data:
        out["days"] = data["Days"]
    return out
