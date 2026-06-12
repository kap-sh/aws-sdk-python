"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TrustStoreStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
    )
)


def to_query_text(value: TrustStoreStatus) -> str:
    return value


def from_query_text(text: str) -> TrustStoreStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TrustStoreStatus value: {text!r}")
    return cast(TrustStoreStatus, text)


def serialize_query(
    value: TrustStoreStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TrustStoreStatus:
    return from_query_text(el.text or "")
