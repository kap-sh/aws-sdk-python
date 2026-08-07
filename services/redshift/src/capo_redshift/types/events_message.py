"""Generated from Smithy shape ``com.amazonaws.redshift#EventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.event_list
    import capo_redshift.types.string


class EventsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    events: NotRequired["capo_redshift.types.event_list.EventList"]
    """<p>A list of <code>Event</code> instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "events" in value:
        import capo_redshift.types.event_list

        capo_redshift.types.event_list.serialize_query(
            value["events"], pairs, f"{key_prefix}Events"
        )


def deserialize_query(el: Element) -> EventsMessage:
    out: EventsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import capo_redshift.types.event_list

        out["events"] = capo_redshift.types.event_list.deserialize_query(child_events)
    return out
