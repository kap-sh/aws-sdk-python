"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeletionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

DeletionMode: TypeAlias = Literal[
    "STANDARD",
    "FORCE_DELETE_STACK",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "FORCE_DELETE_STACK",
    )
)


def to_query_text(value: DeletionMode) -> str:
    return value


def from_query_text(text: str) -> DeletionMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DeletionMode value: {text!r}")
    return cast(DeletionMode, text)


def serialize_query(
    value: DeletionMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeletionMode:
    return from_query_text(el.text or "")
