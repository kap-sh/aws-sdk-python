"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class SegmentCondition(TypedDict, closed=True):
    segment_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the segment to associate with the activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentCondition) -> dict:
    out: dict = {}
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    return out


def deserialize_json(data: dict) -> SegmentCondition:
    out: SegmentCondition = {}  # type: ignore[typeddict-item]
    if "SegmentId" in data:
        out["segment_id"] = data["SegmentId"]
    return out
