"""Generated from Smithy shape ``com.amazonaws.elasticache#AZMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

AZMode: TypeAlias = Literal[
    "single-az",
    "cross-az",
]


# --- awsQuery ser/de ---
def to_query_text(value: AZMode) -> str:
    return value


def from_query_text(text: str) -> AZMode:
    return cast(AZMode, text)


def serialize_query(value: AZMode, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AZMode:
    return from_query_text(el.text or "")
