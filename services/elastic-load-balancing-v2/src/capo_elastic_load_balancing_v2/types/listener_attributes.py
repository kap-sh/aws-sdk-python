"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ListenerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listener_attribute

ListenerAttributes: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.listener_attribute.ListenerAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ListenerAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.listener_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.listener_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ListenerAttributes:
    import capo_elastic_load_balancing_v2.types.listener_attribute

    out: ListenerAttributes = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.listener_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ListenerAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.listener_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.listener_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ListenerAttributes:
    import capo_elastic_load_balancing_v2.types.listener_attribute

    out: ListenerAttributes = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.listener_attribute.deserialize_query(
                child
            )
        )
    return out
