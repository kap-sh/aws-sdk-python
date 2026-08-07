"""Generated from Smithy shape ``com.amazonaws.neptune#EventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.event_list
    import capo_neptune.types.string


class EventsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous Events request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>"""
    events: NotRequired["capo_neptune.types.event_list.EventList"]
    """<p> A list of <a>Event</a> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "events" in value:
        import capo_neptune.types.event_list

        capo_neptune.types.event_list.serialize_query(
            value["events"], pairs, f"{key_prefix}Events"
        )


def deserialize_query(el: Element) -> EventsMessage:
    out: EventsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import capo_neptune.types.event_list

        out["events"] = capo_neptune.types.event_list.deserialize_query(child_events)
    return out
