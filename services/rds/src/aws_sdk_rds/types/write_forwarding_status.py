"""Generated from Smithy shape ``com.amazonaws.rds#WriteForwardingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

WriteForwardingStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
    "unknown",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "enabling",
        "disabling",
        "unknown",
    )
)


def to_query_text(value: WriteForwardingStatus) -> str:
    return value


def from_query_text(text: str) -> WriteForwardingStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown WriteForwardingStatus value: {text!r}")
    return cast(WriteForwardingStatus, text)


def serialize_query(
    value: WriteForwardingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> WriteForwardingStatus:
    return from_query_text(el.text or "")
