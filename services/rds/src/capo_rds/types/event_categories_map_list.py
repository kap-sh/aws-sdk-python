"""Generated from Smithy shape ``com.amazonaws.rds#EventCategoriesMapList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.event_categories_map

EventCategoriesMapList: TypeAlias = list[
    "capo_rds.types.event_categories_map.EventCategoriesMap"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventCategoriesMapList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.event_categories_map

    for n, item in enumerate(value, 1):
        capo_rds.types.event_categories_map.serialize_query(
            item, pairs, f"{prefix}.EventCategoriesMap.{n}"
        )


def deserialize_query(el: Element) -> EventCategoriesMapList:
    import capo_rds.types.event_categories_map

    out: EventCategoriesMapList = []
    for child in el.findall("EventCategoriesMap"):
        out.append(capo_rds.types.event_categories_map.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventCategoriesMapList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.event_categories_map

    for n, item in enumerate(value, 1):
        capo_rds.types.event_categories_map.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EventCategoriesMapList:
    import capo_rds.types.event_categories_map

    out: EventCategoriesMapList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.event_categories_map.deserialize_query(child))
    return out
