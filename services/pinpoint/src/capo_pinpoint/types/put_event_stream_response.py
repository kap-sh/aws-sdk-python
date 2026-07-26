"""Generated from Smithy shape ``com.amazonaws.pinpoint#PutEventStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.event_stream


class PutEventStreamResponse(TypedDict, closed=True):
    event_stream: NotRequired["capo_pinpoint.types.event_stream.EventStream"]


# --- restJson1 ser/de ---
def serialize_json(value: PutEventStreamResponse) -> dict:
    out: dict = {}
    if "event_stream" in value:
        import capo_pinpoint.types.event_stream

        out["EventStream"] = capo_pinpoint.types.event_stream.serialize_json(
            value["event_stream"]
        )
    return out


def deserialize_json(data: dict) -> PutEventStreamResponse:
    out: PutEventStreamResponse = {}  # type: ignore[typeddict-item]
    if "EventStream" in data:
        import capo_pinpoint.types.event_stream

        out["event_stream"] = capo_pinpoint.types.event_stream.deserialize_json(
            data["EventStream"]
        )
    return out
