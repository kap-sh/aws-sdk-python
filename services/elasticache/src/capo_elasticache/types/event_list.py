"""Generated from Smithy shape ``com.amazonaws.elasticache#EventList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.event

EventList: TypeAlias = list["capo_elasticache.types.event.Event"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.event

    for n, item in enumerate(value, 1):
        capo_elasticache.types.event.serialize_query(item, pairs, f"{prefix}.Event.{n}")


def deserialize_query(el: Element) -> EventList:
    import capo_elasticache.types.event

    out: EventList = []
    for child in el.findall("Event"):
        out.append(capo_elasticache.types.event.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.event

    for n, item in enumerate(value, 1):
        capo_elasticache.types.event.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EventList:
    import capo_elasticache.types.event

    out: EventList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.event.deserialize_query(child))
    return out
