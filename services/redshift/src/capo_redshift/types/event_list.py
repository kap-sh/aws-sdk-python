"""Generated from Smithy shape ``com.amazonaws.redshift#EventList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.event

EventList: TypeAlias = list["capo_redshift.types.event.Event"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.event

    for n, item in enumerate(value, 1):
        capo_redshift.types.event.serialize_query(item, pairs, f"{prefix}.Event.{n}")


def deserialize_query(el: Element) -> EventList:
    import capo_redshift.types.event

    out: EventList = []
    for child in el.findall("Event"):
        out.append(capo_redshift.types.event.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.event

    for n, item in enumerate(value, 1):
        capo_redshift.types.event.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EventList:
    import capo_redshift.types.event

    out: EventList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.event.deserialize_query(child))
    return out
