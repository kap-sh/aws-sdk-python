"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ResourceAttribute: TypeAlias = Literal[
    "Properties",
    "Metadata",
    "CreationPolicy",
    "UpdatePolicy",
    "DeletionPolicy",
    "UpdateReplacePolicy",
    "Tags",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Properties",
        "Metadata",
        "CreationPolicy",
        "UpdatePolicy",
        "DeletionPolicy",
        "UpdateReplacePolicy",
        "Tags",
    )
)


def to_query_text(value: ResourceAttribute) -> str:
    return value


def from_query_text(text: str) -> ResourceAttribute:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ResourceAttribute value: {text!r}")
    return cast(ResourceAttribute, text)


def serialize_query(
    value: ResourceAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceAttribute:
    return from_query_text(el.text or "")
