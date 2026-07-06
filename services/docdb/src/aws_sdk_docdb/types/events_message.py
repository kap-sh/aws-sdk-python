"""Generated from Smithy shape ``com.amazonaws.docdb#EventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.event_list
    import aws_sdk_docdb.types.string


class EventsMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    events: NotRequired["aws_sdk_docdb.types.event_list.EventList"]
    """<p>Detailed information about one or more events. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "events" in value:
        import aws_sdk_docdb.types.event_list

        aws_sdk_docdb.types.event_list.serialize_query(
            value["events"], pairs, f"{prefix}.Events"
        )


def deserialize_query(el: Element) -> EventsMessage:
    out: EventsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import aws_sdk_docdb.types.event_list

        out["events"] = aws_sdk_docdb.types.event_list.deserialize_query(child_events)
    return out
