"""Generated from Smithy shape ``com.amazonaws.rds#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

IntegrationStatus: TypeAlias = Literal[
    "creating",
    "active",
    "modifying",
    "failed",
    "deleting",
    "syncing",
    "needs_attention",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "active",
        "modifying",
        "failed",
        "deleting",
        "syncing",
        "needs_attention",
    )
)


def to_query_text(value: IntegrationStatus) -> str:
    return value


def from_query_text(text: str) -> IntegrationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatus value: {text!r}")
    return cast(IntegrationStatus, text)


def serialize_query(
    value: IntegrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IntegrationStatus:
    return from_query_text(el.text or "")
