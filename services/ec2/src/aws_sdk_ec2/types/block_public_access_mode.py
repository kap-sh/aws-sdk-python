"""Generated from Smithy shape ``com.amazonaws.ec2#BlockPublicAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

BlockPublicAccessMode: TypeAlias = Literal[
    "off",
    "block-bidirectional",
    "block-ingress",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: BlockPublicAccessMode) -> str:
    return value


def from_ec2_query_text(text: str) -> BlockPublicAccessMode:
    return cast(BlockPublicAccessMode, text)


def serialize_ec2_query(
    value: BlockPublicAccessMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BlockPublicAccessMode:
    return from_ec2_query_text(el.text or "")
