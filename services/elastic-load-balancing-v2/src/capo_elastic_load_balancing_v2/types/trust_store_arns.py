"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreArns``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_store_arn

TrustStoreArns: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStoreArns, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> TrustStoreArns:
    out: TrustStoreArns = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: TrustStoreArns, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> TrustStoreArns:
    out: TrustStoreArns = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
