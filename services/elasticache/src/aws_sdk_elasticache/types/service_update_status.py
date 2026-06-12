"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

ServiceUpdateStatus: TypeAlias = Literal[
    "available",
    "cancelled",
    "expired",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "cancelled",
        "expired",
    )
)


def to_query_text(value: ServiceUpdateStatus) -> str:
    return value


def from_query_text(text: str) -> ServiceUpdateStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceUpdateStatus value: {text!r}")
    return cast(ServiceUpdateStatus, text)


def serialize_query(
    value: ServiceUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ServiceUpdateStatus:
    return from_query_text(el.text or "")
