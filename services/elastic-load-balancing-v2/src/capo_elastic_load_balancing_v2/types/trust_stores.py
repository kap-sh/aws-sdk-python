"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStores``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_store

TrustStores: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.trust_store.TrustStore"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStores, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.trust_store

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.trust_store.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TrustStores:
    import capo_elastic_load_balancing_v2.types.trust_store

    out: TrustStores = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.trust_store.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TrustStores, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.trust_store

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.trust_store.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrustStores:
    import capo_elastic_load_balancing_v2.types.trust_store

    out: TrustStores = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.trust_store.deserialize_query(child)
        )
    return out
