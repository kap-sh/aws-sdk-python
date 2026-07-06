"""Generated from Smithy shape ``com.amazonaws.redshift#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.event_categories_list
    import aws_sdk_redshift.types.source_type
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class Event(TypedDict, closed=True):
    source_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier for the source of the event.</p>"""
    source_type: NotRequired["aws_sdk_redshift.types.source_type.SourceType"]
    """<p>The source type for this event.</p>"""
    message: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The text of this event.</p>"""
    event_categories: NotRequired[
        "aws_sdk_redshift.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A list of the event categories.</p> <p>Values: Configuration, Management, Monitoring, Security, Pending</p>"""
    severity: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The severity of the event.</p> <p>Values: ERROR, INFO</p>"""
    date: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date and time of the event.</p>"""
    event_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the event.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Event, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "source_identifier" in value:
        pairs.append((f"{prefix}.SourceIdentifier", str(value["source_identifier"])))
    if "source_type" in value:
        import aws_sdk_redshift.types.source_type

        aws_sdk_redshift.types.source_type.serialize_query(
            value["source_type"], pairs, f"{prefix}.SourceType"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "event_categories" in value:
        import aws_sdk_redshift.types.event_categories_list

        aws_sdk_redshift.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{prefix}.EventCategories"
        )
    if "severity" in value:
        pairs.append((f"{prefix}.Severity", str(value["severity"])))
    if "date" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["date"], pairs, f"{prefix}.Date"
        )
    if "event_id" in value:
        pairs.append((f"{prefix}.EventId", str(value["event_id"])))


def deserialize_query(el: Element) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import aws_sdk_redshift.types.source_type

        out["source_type"] = aws_sdk_redshift.types.source_type.deserialize_query(
            child_source_type
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import aws_sdk_redshift.types.event_categories_list

        out["event_categories"] = (
            aws_sdk_redshift.types.event_categories_list.deserialize_query(
                child_event_categories
            )
        )
    child_severity = el.find("Severity")
    if child_severity is not None:
        out["severity"] = str(child_severity.text or "")
    child_date = el.find("Date")
    if child_date is not None:
        import aws_sdk_redshift.types.t_stamp

        out["date"] = aws_sdk_redshift.types.t_stamp.deserialize_query(child_date)
    child_event_id = el.find("EventId")
    if child_event_id is not None:
        out["event_id"] = str(child_event_id.text or "")
    return out
