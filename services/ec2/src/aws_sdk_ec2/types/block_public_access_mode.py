"""Generated from Smithy shape ``com.amazonaws.ec2#BlockPublicAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

BlockPublicAccessMode: TypeAlias = Literal[
    "off",
    "block-bidirectional",
    "block-ingress",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "off",
        "block-bidirectional",
        "block-ingress",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "off",
        "block-bidirectional",
        "block-ingress",
    )
)


def to_ec2_query_text(value: BlockPublicAccessMode) -> str:
    return value


def from_ec2_query_text(text: str) -> BlockPublicAccessMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BlockPublicAccessMode value: {text!r}")
    return cast(BlockPublicAccessMode, text)


def serialize_ec2_query(
    value: BlockPublicAccessMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BlockPublicAccessMode:
    return from_ec2_query_text(el.text or "")
