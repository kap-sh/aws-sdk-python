"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

TrustStoreStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
]


# --- awsQuery ser/de ---
def to_query_text(value: TrustStoreStatus) -> str:
    return value


def from_query_text(text: str) -> TrustStoreStatus:
    return cast(TrustStoreStatus, text)


def serialize_query(
    value: TrustStoreStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TrustStoreStatus:
    return from_query_text(el.text or "")
