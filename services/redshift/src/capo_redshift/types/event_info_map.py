"""Generated from Smithy shape ``com.amazonaws.redshift#EventInfoMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.event_categories_list
    import capo_redshift.types.string


class EventInfoMap(TypedDict, closed=True):
    event_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of an Amazon Redshift event.</p>"""
    event_categories: NotRequired[
        "capo_redshift.types.event_categories_list.EventCategoriesList"
    ]
    """<p>The category of an Amazon Redshift event.</p>"""
    event_description: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of an Amazon Redshift event.</p>"""
    severity: NotRequired["capo_redshift.types.string.String"]
    """<p>The severity of the event.</p> <p>Values: ERROR, INFO</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventInfoMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "event_id" in value:
        pairs.append((f"{key_prefix}EventId", str(value["event_id"])))
    if "event_categories" in value:
        import capo_redshift.types.event_categories_list

        capo_redshift.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{key_prefix}EventCategories"
        )
    if "event_description" in value:
        pairs.append((f"{key_prefix}EventDescription", str(value["event_description"])))
    if "severity" in value:
        pairs.append((f"{key_prefix}Severity", str(value["severity"])))


def deserialize_query(el: Element) -> EventInfoMap:
    out: EventInfoMap = {}  # type: ignore[typeddict-item]
    child_event_id = el.find("EventId")
    if child_event_id is not None:
        out["event_id"] = str(child_event_id.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import capo_redshift.types.event_categories_list

        out["event_categories"] = (
            capo_redshift.types.event_categories_list.deserialize_query(
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
