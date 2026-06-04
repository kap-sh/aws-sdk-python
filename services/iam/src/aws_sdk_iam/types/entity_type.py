"""Generated from Smithy shape ``com.amazonaws.iam#EntityType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

EntityType: TypeAlias = Literal[
    "User",
    "Role",
    "Group",
    "LocalManagedPolicy",
    "AWSManagedPolicy",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "User",
        "Role",
        "Group",
        "LocalManagedPolicy",
        "AWSManagedPolicy",
    )
)


def to_query_text(value: EntityType) -> str:
    return value


def from_query_text(text: str) -> EntityType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {text!r}")
    return cast(EntityType, text)


def serialize_query(
    value: EntityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EntityType:
    return from_query_text(el.text or "")
