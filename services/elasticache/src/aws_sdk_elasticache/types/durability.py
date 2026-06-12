"""Generated from Smithy shape ``com.amazonaws.elasticache#Durability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

Durability: TypeAlias = Literal[
    "default",
    "async",
    "sync",
    "disabled",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "async",
        "sync",
        "disabled",
    )
)


def to_query_text(value: Durability) -> str:
    return value


def from_query_text(text: str) -> Durability:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Durability value: {text!r}")
    return cast(Durability, text)


def serialize_query(
    value: Durability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Durability:
    return from_query_text(el.text or "")
