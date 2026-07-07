"""Generated from Smithy shape ``com.amazonaws.redshift#EventInfoMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.event_categories_list
    import aws_sdk_redshift.types.string


class EventInfoMap(TypedDict, closed=True):
    event_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of an Amazon Redshift event.</p>"""
    event_categories: NotRequired[
        "aws_sdk_redshift.types.event_categories_list.EventCategoriesList"
    ]
    """<p>The category of an Amazon Redshift event.</p>"""
    event_description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of an Amazon Redshift event.</p>"""
    severity: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The severity of the event.</p> <p>Values: ERROR, INFO</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventInfoMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_id" in value:
        pairs.append((f"{prefix}.EventId", str(value["event_id"])))
    if "event_categories" in value:
        import aws_sdk_redshift.types.event_categories_list

        aws_sdk_redshift.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{prefix}.EventCategories"
        )
    if "event_description" in value:
        pairs.append((f"{prefix}.EventDescription", str(value["event_description"])))
    if "severity" in value:
        pairs.append((f"{prefix}.Severity", str(value["severity"])))


def deserialize_query(el: Element) -> EventInfoMap:
    out: EventInfoMap = {}  # type: ignore[typeddict-item]
    child_event_id = el.find("EventId")
    if child_event_id is not None:
        out["event_id"] = str(child_event_id.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import aws_sdk_redshift.types.event_categories_list

        out["event_categories"] = (
            aws_sdk_redshift.types.event_categories_list.deserialize_query(
                child_event_categories
            )
        )
    child_event_description = el.find("EventDescription")
    if child_event_description is not None:
        out["event_description"] = str(child_event_description.text or "")
    child_severity = el.find("Severity")
    if child_severity is not None:
        out["severity"] = str(child_severity.text or "")
    return out
