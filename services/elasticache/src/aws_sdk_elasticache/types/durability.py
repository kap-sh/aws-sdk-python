"""Generated from Smithy shape ``com.amazonaws.elasticache#Durability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

Durability: TypeAlias = Literal[
    "default",
    "async",
    "sync",
    "disabled",
]


# --- awsQuery ser/de ---
def to_query_text(value: Durability) -> str:
    return value


def from_query_text(text: str) -> Durability:
    return cast(Durability, text)


def serialize_query(
    value: Durability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Durability:
    return from_query_text(el.text or "")
