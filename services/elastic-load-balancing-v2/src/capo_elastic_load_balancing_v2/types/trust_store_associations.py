"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_store_association

TrustStoreAssociations: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.trust_store_association.TrustStoreAssociation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStoreAssociations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.trust_store_association

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.trust_store_association.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TrustStoreAssociations:
    import capo_elastic_load_balancing_v2.types.trust_store_association

    out: TrustStoreAssociations = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.trust_store_association.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TrustStoreAssociations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.trust_store_association

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.trust_store_association.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrustStoreAssociations:
    import capo_elastic_load_balancing_v2.types.trust_store_association

    out: TrustStoreAssociations = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.trust_store_association.deserialize_query(
                child
            )
        )
    return out
