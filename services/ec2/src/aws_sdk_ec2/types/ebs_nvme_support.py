"""Generated from Smithy shape ``com.amazonaws.ec2#EbsNvmeSupport``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

EbsNvmeSupport: TypeAlias = Literal[
    "unsupported",
    "supported",
    "required",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EbsNvmeSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> EbsNvmeSupport:
    return cast(EbsNvmeSupport, text)


def serialize_ec2_query(
    value: EbsNvmeSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EbsNvmeSupport:
    return from_ec2_query_text(el.text or "")
