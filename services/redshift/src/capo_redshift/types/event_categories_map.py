"""Generated from Smithy shape ``com.amazonaws.redshift#EventCategoriesMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.event_info_map_list
    import capo_redshift.types.string


class EventCategoriesMap(TypedDict, closed=True):
    source_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The source type, such as cluster or cluster-snapshot, that the returned categories belong to.</p>"""
    events: NotRequired["capo_redshift.types.event_info_map_list.EventInfoMapList"]
    """<p>The events in the event category.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventCategoriesMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_type" in value:
        pairs.append((f"{prefix}.SourceType", str(value["source_type"])))
    if "events" in value:
        import capo_redshift.types.event_info_map_list

        capo_redshift.types.event_info_map_list.serialize_query(
            value["events"], pairs, f"{prefix}.Events"
        )


def deserialize_query(el: Element) -> EventCategoriesMap:
    out: EventCategoriesMap = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    child_events = el.find("Events")
    if child_events is not None:
        import capo_redshift.types.event_info_map_list

        out["events"] = capo_redshift.types.event_info_map_list.deserialize_query(
            child_events
        )
    return out
