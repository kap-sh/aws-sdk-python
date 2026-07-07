"""Generated from Smithy shape ``com.amazonaws.pinpoint#ClosedDaysRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class ClosedDaysRule(TypedDict, closed=True):
    name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the closed day rule.</p>"""
    start_date_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Start DateTime ISO 8601 format</p>"""
    end_date_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>End DateTime ISO 8601 format</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClosedDaysRule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "start_date_time" in value:
        out["StartDateTime"] = value["start_date_time"]
    if "end_date_time" in value:
        out["EndDateTime"] = value["end_date_time"]
    return out


def deserialize_json(data: dict) -> ClosedDaysRule:
    out: ClosedDaysRule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "StartDateTime" in data:
        out["start_date_time"] = data["StartDateTime"]
    if "EndDateTime" in data:
        out["end_date_time"] = data["EndDateTime"]
    return out
