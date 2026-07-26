"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateEventActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.action
    import capo_dataexchange.types.event
    import capo_dataexchange.types.map_of__string


class CreateEventActionRequest(TypedDict, closed=True):
    action: "capo_dataexchange.types.action.Action"
    """<p>What occurs after a certain event.</p>"""
    event: "capo_dataexchange.types.event.Event"
    """<p>What occurs to start an action.</p>"""
    tags: NotRequired["capo_dataexchange.types.map_of__string.MapOf__string"]
    """<p>Key-value pairs that you can associate with the event action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventActionRequest) -> dict:
    out: dict = {}
    import capo_dataexchange.types.action

    out["Action"] = capo_dataexchange.types.action.serialize_json(value["action"])
    import capo_dataexchange.types.event

    out["Event"] = capo_dataexchange.types.event.serialize_json(value["event"])
    if "tags" in value:
        import capo_dataexchange.types.map_of__string

        out["Tags"] = capo_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEventActionRequest:
    out: CreateEventActionRequest = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_dataexchange.types.action

        out["action"] = capo_dataexchange.types.action.deserialize_json(data["Action"])
    else:
        raise DeserializationError("CreateEventActionRequest.action required")
    if "Event" in data:
        import capo_dataexchange.types.event

        out["event"] = capo_dataexchange.types.event.deserialize_json(data["Event"])
    else:
        raise DeserializationError("CreateEventActionRequest.event required")
    if "Tags" in data:
        import capo_dataexchange.types.map_of__string

        out["tags"] = capo_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    return out
