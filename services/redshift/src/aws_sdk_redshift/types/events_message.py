"""Generated from Smithy shape ``com.amazonaws.redshift#EventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.event_list
    import aws_sdk_redshift.types.string


class EventsMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    events: NotRequired["aws_sdk_redshift.types.event_list.EventList"]
    """<p>A list of <code>Event</code> instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "events" in value:
        import aws_sdk_redshift.types.event_list

        aws_sdk_redshift.types.event_list.serialize_query(
            value["events"], pairs, f"{prefix}.Events"
        )


def deserialize_query(el: Element) -> EventsMessage:
    out: EventsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import aws_sdk_redshift.types.event_list

        out["events"] = aws_sdk_redshift.types.event_list.deserialize_query(
            child_events
        )
    return out
