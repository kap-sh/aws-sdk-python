"""Generated from Smithy shape ``com.amazonaws.elasticache#EffectiveDurability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

EffectiveDurability: TypeAlias = Literal[
    "async",
    "sync",
    "disabled",
]


# --- awsQuery ser/de ---
def to_query_text(value: EffectiveDurability) -> str:
    return value


def from_query_text(text: str) -> EffectiveDurability:
    return cast(EffectiveDurability, text)


def serialize_query(
    value: EffectiveDurability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EffectiveDurability:
    return from_query_text(el.text or "")
