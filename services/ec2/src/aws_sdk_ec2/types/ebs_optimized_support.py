"""Generated from Smithy shape ``com.amazonaws.ec2#EbsOptimizedSupport``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

EbsOptimizedSupport: TypeAlias = Literal[
    "unsupported",
    "supported",
    "default",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EbsOptimizedSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> EbsOptimizedSupport:
    return cast(EbsOptimizedSupport, text)


def serialize_ec2_query(
    value: EbsOptimizedSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EbsOptimizedSupport:
    return from_ec2_query_text(el.text or "")
