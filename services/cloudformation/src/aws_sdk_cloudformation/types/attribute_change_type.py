"""Generated from Smithy shape ``com.amazonaws.cloudformation#AttributeChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

AttributeChangeType: TypeAlias = Literal[
    "Add",
    "Remove",
    "Modify",
    "SyncWithActual",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Add",
        "Remove",
        "Modify",
        "SyncWithActual",
    )
)


def to_query_text(value: AttributeChangeType) -> str:
    return value


def from_query_text(text: str) -> AttributeChangeType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AttributeChangeType value: {text!r}")
    return cast(AttributeChangeType, text)


def serialize_query(
    value: AttributeChangeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AttributeChangeType:
    return from_query_text(el.text or "")
