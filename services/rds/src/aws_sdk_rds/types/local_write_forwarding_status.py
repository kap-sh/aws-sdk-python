"""Generated from Smithy shape ``com.amazonaws.rds#LocalWriteForwardingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

LocalWriteForwardingStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
    "requested",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "enabling",
        "disabling",
        "requested",
    )
)


def to_query_text(value: LocalWriteForwardingStatus) -> str:
    return value


def from_query_text(text: str) -> LocalWriteForwardingStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown LocalWriteForwardingStatus value: {text!r}"
        )
    return cast(LocalWriteForwardingStatus, text)


def serialize_query(
    value: LocalWriteForwardingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LocalWriteForwardingStatus:
    return from_query_text(el.text or "")
