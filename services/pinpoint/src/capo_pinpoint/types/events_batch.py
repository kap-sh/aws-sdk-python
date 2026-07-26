"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventsBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.map_of_event
    import capo_pinpoint.types.public_endpoint


class EventsBatch(TypedDict, closed=True):
    endpoint: NotRequired["capo_pinpoint.types.public_endpoint.PublicEndpoint"]
    """<p>A set of properties and attributes that are associated with the endpoint.</p>"""
    events: NotRequired["capo_pinpoint.types.map_of_event.MapOfEvent"]
    """<p>A set of properties that are associated with the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventsBatch) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import capo_pinpoint.types.public_endpoint

        out["Endpoint"] = capo_pinpoint.types.public_endpoint.serialize_json(
            value["endpoint"]
        )
    if "events" in value:
        import capo_pinpoint.types.map_of_event

        out["Events"] = capo_pinpoint.types.map_of_event.serialize_json(value["events"])
    return out


def deserialize_json(data: dict) -> EventsBatch:
    out: EventsBatch = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        import capo_pinpoint.types.public_endpoint

        out["endpoint"] = capo_pinpoint.types.public_endpoint.deserialize_json(
            data["Endpoint"]
        )
    if "Events" in data:
        import capo_pinpoint.types.map_of_event

        out["events"] = capo_pinpoint.types.map_of_event.deserialize_json(
            data["Events"]
        )
    return out
