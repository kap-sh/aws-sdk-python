"""Generated from Smithy shape ``com.amazonaws.docdb#EventCategoriesMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.event_categories_map_list


class EventCategoriesMessage(TypedDict):
    event_categories_map_list: NotRequired[
        "aws_sdk_docdb.types.event_categories_map_list.EventCategoriesMapList"
    ]
    """<p>A list of event category maps.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventCategoriesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_categories_map_list" in value:
        import aws_sdk_docdb.types.event_categories_map_list

        aws_sdk_docdb.types.event_categories_map_list.serialize_query(
            value["event_categories_map_list"],
            pairs,
            f"{prefix}.EventCategoriesMapList",
        )


def deserialize_query(el: Element) -> EventCategoriesMessage:
    out: EventCategoriesMessage = {}  # type: ignore[typeddict-item]
    child_event_categories_map_list = el.find("EventCategoriesMapList")
    if child_event_categories_map_list is not None:
        import aws_sdk_docdb.types.event_categories_map_list

        out["event_categories_map_list"] = (
            aws_sdk_docdb.types.event_categories_map_list.deserialize_query(
                child_event_categories_map_list
            )
        )
    return out
