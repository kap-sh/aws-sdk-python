"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreAssociationStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TrustStoreAssociationStatusEnum: TypeAlias = Literal[
    "active",
    "removed",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "removed",
    )
)


def to_query_text(value: TrustStoreAssociationStatusEnum) -> str:
    return value


def from_query_text(text: str) -> TrustStoreAssociationStatusEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TrustStoreAssociationStatusEnum value: {text!r}"
        )
    return cast(TrustStoreAssociationStatusEnum, text)


def serialize_query(
    value: TrustStoreAssociationStatusEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TrustStoreAssociationStatusEnum:
    return from_query_text(el.text or "")
