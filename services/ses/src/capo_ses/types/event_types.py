"""Generated from Smithy shape ``com.amazonaws.ses#EventTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.event_type

EventTypes: TypeAlias = list["capo_ses.types.event_type.EventType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.event_type

    for n, item in enumerate(value, 1):
        capo_ses.types.event_type.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> EventTypes:
    import capo_ses.types.event_type

    out: EventTypes = []
    for child in el.findall("member"):
        out.append(capo_ses.types.event_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.event_type

    for n, item in enumerate(value, 1):
        capo_ses.types.event_type.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EventTypes:
    import capo_ses.types.event_type

    out: EventTypes = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.event_type.deserialize_query(child))
    return out
