"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.map_of_events_batch


class EventsRequest(TypedDict, closed=True):
    batch_item: NotRequired["capo_pinpoint.types.map_of_events_batch.MapOfEventsBatch"]
    """<p>The batch of events to process. For each item in a batch, the endpoint ID acts as a key that has an EventsBatch object as its value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventsRequest) -> dict:
    out: dict = {}
    if "batch_item" in value:
        import capo_pinpoint.types.map_of_events_batch

        out["BatchItem"] = capo_pinpoint.types.map_of_events_batch.serialize_json(
            value["batch_item"]
        )
    return out


def deserialize_json(data: dict) -> EventsRequest:
    out: EventsRequest = {}  # type: ignore[typeddict-item]
    if "BatchItem" in data:
        import capo_pinpoint.types.map_of_events_batch

        out["batch_item"] = capo_pinpoint.types.map_of_events_batch.deserialize_json(
            data["BatchItem"]
        )
    return out
