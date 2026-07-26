"""Generated from Smithy shape ``com.amazonaws.redshift#EventInfoMapList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.event_info_map

EventInfoMapList: TypeAlias = list["capo_redshift.types.event_info_map.EventInfoMap"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventInfoMapList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.event_info_map

    for n, item in enumerate(value, 1):
        capo_redshift.types.event_info_map.serialize_query(
            item, pairs, f"{prefix}.EventInfoMap.{n}"
        )


def deserialize_query(el: Element) -> EventInfoMapList:
    import capo_redshift.types.event_info_map

    out: EventInfoMapList = []
    for child in el.findall("EventInfoMap"):
        out.append(capo_redshift.types.event_info_map.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventInfoMapList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.event_info_map

    for n, item in enumerate(value, 1):
        capo_redshift.types.event_info_map.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EventInfoMapList:
    import capo_redshift.types.event_info_map

    out: EventInfoMapList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.event_info_map.deserialize_query(child))
    return out
