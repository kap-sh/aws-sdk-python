"""Generated from Smithy shape ``com.amazonaws.elasticache#EventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.event_list
    import capo_elasticache.types.string


class EventsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    events: NotRequired["capo_elasticache.types.event_list.EventList"]
    """<p>A list of events. Each element in the list contains detailed information about one event.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "events" in value:
        import capo_elasticache.types.event_list

        capo_elasticache.types.event_list.serialize_query(
            value["events"], pairs, f"{prefix}.Events"
        )


def deserialize_query(el: Element) -> EventsMessage:
    out: EventsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import capo_elasticache.types.event_list

        out["events"] = capo_elasticache.types.event_list.deserialize_query(
            child_events
        )
    return out
