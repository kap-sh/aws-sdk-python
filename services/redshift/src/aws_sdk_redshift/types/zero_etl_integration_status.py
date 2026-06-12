"""Generated from Smithy shape ``com.amazonaws.redshift#ZeroETLIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ZeroETLIntegrationStatus: TypeAlias = Literal[
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


def to_query_text(value: ZeroETLIntegrationStatus) -> str:
    return value


def from_query_text(text: str) -> ZeroETLIntegrationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ZeroETLIntegrationStatus value: {text!r}")
    return cast(ZeroETLIntegrationStatus, text)


def serialize_query(
    value: ZeroETLIntegrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ZeroETLIntegrationStatus:
    return from_query_text(el.text or "")
