"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ChangeSetType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "IMPORT",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "UPDATE",
        "IMPORT",
    )
)


def to_query_text(value: ChangeSetType) -> str:
    return value


def from_query_text(text: str) -> ChangeSetType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChangeSetType value: {text!r}")
    return cast(ChangeSetType, text)


def serialize_query(
    value: ChangeSetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeSetType:
    return from_query_text(el.text or "")
