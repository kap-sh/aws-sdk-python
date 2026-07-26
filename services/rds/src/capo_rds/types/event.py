"""Generated from Smithy shape ``com.amazonaws.rds#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.event_categories_list
    import capo_rds.types.source_type
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class Event(TypedDict, closed=True):
    source_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the identifier for the source of the event.</p>"""
    source_type: NotRequired["capo_rds.types.source_type.SourceType"]
    """<p>Specifies the source type for this event.</p>"""
    message: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the text of this event.</p>"""
    event_categories: NotRequired[
        "capo_rds.types.event_categories_list.EventCategoriesList"
    ]
    """<p>Specifies the category for the event.</p>"""
    date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>Specifies the date and time of the event.</p>"""
    source_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the event.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Event, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "source_identifier" in value:
        pairs.append((f"{prefix}.SourceIdentifier", str(value["source_identifier"])))
    if "source_type" in value:
        import capo_rds.types.source_type

        capo_rds.types.source_type.serialize_query(
            value["source_type"], pairs, f"{prefix}.SourceType"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "event_categories" in value:
        import capo_rds.types.event_categories_list

        capo_rds.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{prefix}.EventCategories"
        )
    if "date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(value["date"], pairs, f"{prefix}.Date")
    if "source_arn" in value:
        pairs.append((f"{prefix}.SourceArn", str(value["source_arn"])))


def deserialize_query(el: Element) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import capo_rds.types.source_type

        out["source_type"] = capo_rds.types.source_type.deserialize_query(
            child_source_type
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import capo_rds.types.event_categories_list

        out["event_categories"] = (
            capo_rds.types.event_categories_list.deserialize_query(
                child_event_categories
            )
        )
    child_date = el.find("Date")
    if child_date is not None:
        import capo_rds.types.t_stamp

        out["date"] = capo_rds.types.t_stamp.deserialize_query(child_date)
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    return out
