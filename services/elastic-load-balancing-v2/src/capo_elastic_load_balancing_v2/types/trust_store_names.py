"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreNames``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_store_name

TrustStoreNames: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.trust_store_name.TrustStoreName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStoreNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> TrustStoreNames:
    out: TrustStoreNames = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: TrustStoreNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> TrustStoreNames:
    out: TrustStoreNames = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
