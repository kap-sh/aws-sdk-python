"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHooksStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ChangeSetHooksStatus: TypeAlias = Literal[
    "PLANNING",
    "PLANNED",
    "UNAVAILABLE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLANNING",
        "PLANNED",
        "UNAVAILABLE",
    )
)


def to_query_text(value: ChangeSetHooksStatus) -> str:
    return value


def from_query_text(text: str) -> ChangeSetHooksStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChangeSetHooksStatus value: {text!r}")
    return cast(ChangeSetHooksStatus, text)


def serialize_query(
    value: ChangeSetHooksStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeSetHooksStatus:
    return from_query_text(el.text or "")
