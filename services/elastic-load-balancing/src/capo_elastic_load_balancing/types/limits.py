"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Limits``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.limit

Limits: TypeAlias = list["capo_elastic_load_balancing.types.limit.Limit"]


# --- awsQuery ser/de ---
def serialize_query(value: Limits, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_elastic_load_balancing.types.limit

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.limit.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Limits:
    import capo_elastic_load_balancing.types.limit

    out: Limits = []
    for child in el.findall("member"):
        out.append(capo_elastic_load_balancing.types.limit.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Limits, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.limit

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.limit.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Limits:
    import capo_elastic_load_balancing.types.limit

    out: Limits = []
    for child in parent.findall(tag):
        out.append(capo_elastic_load_balancing.types.limit.deserialize_query(child))
    return out
