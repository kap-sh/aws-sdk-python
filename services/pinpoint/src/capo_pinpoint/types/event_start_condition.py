"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventStartCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.event_filter


class EventStartCondition(TypedDict, closed=True):
    event_filter: NotRequired["capo_pinpoint.types.event_filter.EventFilter"]
    segment_id: NotRequired["capo_pinpoint.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: EventStartCondition) -> dict:
    out: dict = {}
    if "event_filter" in value:
        import capo_pinpoint.types.event_filter

        out["EventFilter"] = capo_pinpoint.types.event_filter.serialize_json(
            value["event_filter"]
        )
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    return out


def deserialize_json(data: dict) -> EventStartCondition:
    out: EventStartCondition = {}  # type: ignore[typeddict-item]
    if "EventFilter" in data:
        import capo_pinpoint.types.event_filter

        out["event_filter"] = capo_pinpoint.types.event_filter.deserialize_json(
            data["EventFilter"]
        )
    if "SegmentId" in data:
        out["segment_id"] = data["SegmentId"]
    return out
