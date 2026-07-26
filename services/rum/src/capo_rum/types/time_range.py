"""Generated from Smithy shape ``com.amazonaws.rum#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rum.types.query_timestamp


class TimeRange(TypedDict, closed=True):
    after: "capo_rum.types.query_timestamp.QueryTimestamp"
    """<p>The beginning of the time range to retrieve performance events from.</p>"""
    before: "capo_rum.types.query_timestamp.QueryTimestamp"
    """<p>The end of the time range to retrieve performance events from. If you omit this, the time range extends to the time that this operation is performed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRange) -> dict:
    out: dict = {}
    out["After"] = value.get("after", 0)
    out["Before"] = value.get("before", 0)
    return out


def deserialize_json(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "After" in data:
        out["after"] = data["After"]
    else:
        out["after"] = 0
    if "Before" in data:
        out["before"] = data["Before"]
    else:
        out["before"] = 0
    return out
