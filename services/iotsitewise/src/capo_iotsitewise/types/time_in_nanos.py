"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeInNanos``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.offset_in_nanos
    import capo_iotsitewise.types.time_in_seconds


class TimeInNanos(TypedDict, closed=True):
    time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds"
    """<p>The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by <code>offsetInNanos</code>.</p>"""
    offset_in_nanos: NotRequired["capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"]
    """<p>The nanosecond offset from <code>timeInSeconds</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeInNanos) -> dict:
    out: dict = {}
    out["timeInSeconds"] = value["time_in_seconds"]
    if "offset_in_nanos" in value:
        out["offsetInNanos"] = value["offset_in_nanos"]
    return out


def deserialize_json(data: dict) -> TimeInNanos:
    out: TimeInNanos = {}  # type: ignore[typeddict-item]
    if "timeInSeconds" in data:
        out["time_in_seconds"] = data["timeInSeconds"]
    else:
        raise DeserializationError("TimeInNanos.time_in_seconds required")
    if "offsetInNanos" in data:
        out["offset_in_nanos"] = data["offsetInNanos"]
    return out
