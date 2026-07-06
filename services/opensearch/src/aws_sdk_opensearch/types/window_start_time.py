"""Generated from Smithy shape ``com.amazonaws.opensearch#WindowStartTime``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.start_time_hours
    import aws_sdk_opensearch.types.start_time_minutes


class WindowStartTime(TypedDict, closed=True):
    hours: "aws_sdk_opensearch.types.start_time_hours.StartTimeHours"
    """<p>The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time. For example, <code>17</code> refers to 5:00 P.M. UTC.</p>"""
    minutes: "aws_sdk_opensearch.types.start_time_minutes.StartTimeMinutes"
    """<p>The start minute of the window, in UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WindowStartTime) -> dict:
    out: dict = {}
    out["Hours"] = value.get("hours", 0)
    out["Minutes"] = value.get("minutes", 0)
    return out


def deserialize_json(data: dict) -> WindowStartTime:
    out: WindowStartTime = {}  # type: ignore[typeddict-item]
    if "Hours" in data:
        out["hours"] = data["Hours"]
    else:
        out["hours"] = 0
    if "Minutes" in data:
        out["minutes"] = data["Minutes"]
    else:
        out["minutes"] = 0
    return out
