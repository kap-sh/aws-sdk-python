"""Generated from Smithy shape ``com.amazonaws.neptune#EventCategoriesMap``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.event_categories_list
    import aws_sdk_neptune.types.string


class EventCategoriesMap(TypedDict):
    source_type: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The source type that the returned categories belong to</p>"""
    event_categories: NotRequired[
        "aws_sdk_neptune.types.event_categories_list.EventCategoriesList"
    ]
    """<p>The event categories for the specified source type</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventCategoriesMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_type" in value:
        pairs.append((f"{prefix}.SourceType", str(value["source_type"])))
    if "event_categories" in value:
        import aws_sdk_neptune.types.event_categories_list

        aws_sdk_neptune.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{prefix}.EventCategories"
        )


def deserialize_query(el: Element) -> EventCategoriesMap:
    out: EventCategoriesMap = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import aws_sdk_neptune.types.event_categories_list

        out["event_categories"] = (
            aws_sdk_neptune.types.event_categories_list.deserialize_query(
                child_event_categories
            )
        )
    return out
