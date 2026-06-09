"""Generated from Smithy shape ``com.amazonaws.ec2#SSEType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

SSEType: TypeAlias = Literal[
    "sse-ebs",
    "sse-kms",
    "none",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sse-ebs",
        "sse-kms",
        "none",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "sse-ebs",
        "sse-kms",
        "none",
    )
)


def to_ec2_query_text(value: SSEType) -> str:
    return value


def from_ec2_query_text(text: str) -> SSEType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SSEType value: {text!r}")
    return cast(SSEType, text)


def serialize_ec2_query(
    value: SSEType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SSEType:
    return from_ec2_query_text(el.text or "")
