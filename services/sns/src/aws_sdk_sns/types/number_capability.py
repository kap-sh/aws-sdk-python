"""Generated from Smithy shape ``com.amazonaws.sns#NumberCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sns._protocol.xml import Element

"""Enum listing out all supported number capabilities."""
NumberCapability: TypeAlias = Literal[
    "SMS",
    "MMS",
    "VOICE",
]


# --- awsQuery ser/de ---
def to_query_text(value: NumberCapability) -> str:
    return value


def from_query_text(text: str) -> NumberCapability:
    return cast(NumberCapability, text)


def serialize_query(
    value: NumberCapability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NumberCapability:
    return from_query_text(el.text or "")
