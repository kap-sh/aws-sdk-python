"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreAssociationStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

TrustStoreAssociationStatusEnum: TypeAlias = Literal[
    "active",
    "removed",
]


# --- awsQuery ser/de ---
def to_query_text(value: TrustStoreAssociationStatusEnum) -> str:
    return value


def from_query_text(text: str) -> TrustStoreAssociationStatusEnum:
    return cast(TrustStoreAssociationStatusEnum, text)


def serialize_query(
    value: TrustStoreAssociationStatusEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TrustStoreAssociationStatusEnum:
    return from_query_text(el.text or "")
