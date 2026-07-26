"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreRevocations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_store_revocation

TrustStoreRevocations: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.trust_store_revocation.TrustStoreRevocation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStoreRevocations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.trust_store_revocation

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.trust_store_revocation.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TrustStoreRevocations:
    import capo_elastic_load_balancing_v2.types.trust_store_revocation

    out: TrustStoreRevocations = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.trust_store_revocation.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TrustStoreRevocations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.trust_store_revocation

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.trust_store_revocation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrustStoreRevocations:
    import capo_elastic_load_balancing_v2.types.trust_store_revocation

    out: TrustStoreRevocations = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.trust_store_revocation.deserialize_query(
                child
            )
        )
    return out
