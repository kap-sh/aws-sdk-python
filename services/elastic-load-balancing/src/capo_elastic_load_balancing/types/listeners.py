"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Listeners``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.listener

Listeners: TypeAlias = list["capo_elastic_load_balancing.types.listener.Listener"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Listeners, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.listener

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.listener.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Listeners:
    import capo_elastic_load_balancing.types.listener

    out: Listeners = []
    for child in el.findall("member"):
        out.append(capo_elastic_load_balancing.types.listener.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Listeners, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.listener

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.listener.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Listeners:
    import capo_elastic_load_balancing.types.listener

    out: Listeners = []
    for child in parent.findall(tag):
        out.append(capo_elastic_load_balancing.types.listener.deserialize_query(child))
    return out
