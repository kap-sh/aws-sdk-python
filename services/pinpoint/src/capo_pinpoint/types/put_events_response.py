"""Generated from Smithy shape ``com.amazonaws.pinpoint#PutEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.events_response


class PutEventsResponse(TypedDict, closed=True):
    events_response: NotRequired["capo_pinpoint.types.events_response.EventsResponse"]


# --- restJson1 ser/de ---
def serialize_json(value: PutEventsResponse) -> dict:
    out: dict = {}
    if "events_response" in value:
        import capo_pinpoint.types.events_response

        out["EventsResponse"] = capo_pinpoint.types.events_response.serialize_json(
            value["events_response"]
        )
    return out


def deserialize_json(data: dict) -> PutEventsResponse:
    out: PutEventsResponse = {}  # type: ignore[typeddict-item]
    if "EventsResponse" in data:
        import capo_pinpoint.types.events_response

        out["events_response"] = capo_pinpoint.types.events_response.deserialize_json(
            data["EventsResponse"]
        )
    return out
