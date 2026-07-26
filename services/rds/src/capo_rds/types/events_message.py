"""Generated from Smithy shape ``com.amazonaws.rds#EventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.event_list
    import capo_rds.types.string


class EventsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous Events request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    events: NotRequired["capo_rds.types.event_list.EventList"]
    """<p>A list of <code>Event</code> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "events" in value:
        import capo_rds.types.event_list

        capo_rds.types.event_list.serialize_query(
            value["events"], pairs, f"{prefix}.Events"
        )


def deserialize_query(el: Element) -> EventsMessage:
    out: EventsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import capo_rds.types.event_list

        out["events"] = capo_rds.types.event_list.deserialize_query(child_events)
    return out
