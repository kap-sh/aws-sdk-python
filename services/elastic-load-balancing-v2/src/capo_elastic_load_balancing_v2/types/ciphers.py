"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Ciphers``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.cipher

Ciphers: TypeAlias = list["capo_elastic_load_balancing_v2.types.cipher.Cipher"]


# --- awsQuery ser/de ---
def serialize_query(value: Ciphers, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_elastic_load_balancing_v2.types.cipher

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.cipher.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Ciphers:
    import capo_elastic_load_balancing_v2.types.cipher

    out: Ciphers = []
    for child in el.findall("member"):
        out.append(capo_elastic_load_balancing_v2.types.cipher.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Ciphers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.cipher

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.cipher.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Ciphers:
    import capo_elastic_load_balancing_v2.types.cipher

    out: Ciphers = []
    for child in parent.findall(tag):
        out.append(capo_elastic_load_balancing_v2.types.cipher.deserialize_query(child))
    return out
