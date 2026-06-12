"""Generated from Smithy shape ``com.amazonaws.sns#NumberCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

"""Enum listing out all supported number capabilities."""
NumberCapability: TypeAlias = Literal[
    "SMS",
    "MMS",
    "VOICE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMS",
        "MMS",
        "VOICE",
    )
)


def to_query_text(value: NumberCapability) -> str:
    return value


def from_query_text(text: str) -> NumberCapability:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NumberCapability value: {text!r}")
    return cast(NumberCapability, text)


def serialize_query(
    value: NumberCapability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NumberCapability:
    return from_query_text(el.text or "")
