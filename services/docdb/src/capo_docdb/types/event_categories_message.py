"""Generated from Smithy shape ``com.amazonaws.docdb#EventCategoriesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.event_categories_map_list


class EventCategoriesMessage(TypedDict, closed=True):
    event_categories_map_list: NotRequired[
        "capo_docdb.types.event_categories_map_list.EventCategoriesMapList"
    ]
    """<p>A list of event category maps.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventCategoriesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "event_categories_map_list" in value:
        import capo_docdb.types.event_categories_map_list

        capo_docdb.types.event_categories_map_list.serialize_query(
            value["event_categories_map_list"],
            pairs,
            f"{key_prefix}EventCategoriesMapList",
        )


def deserialize_query(el: Element) -> EventCategoriesMessage:
    out: EventCategoriesMessage = {}  # type: ignore[typeddict-item]
    child_event_categories_map_list = el.find("EventCategoriesMapList")
    if child_event_categories_map_list is not None:
        import capo_docdb.types.event_categories_map_list

        out["event_categories_map_list"] = (
            capo_docdb.types.event_categories_map_list.deserialize_query(
                child_event_categories_map_list
            )
        )
    return out
