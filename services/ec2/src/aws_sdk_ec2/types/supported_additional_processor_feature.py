"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedAdditionalProcessorFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SupportedAdditionalProcessorFeature: TypeAlias = Literal[
    "amd-sev-snp",
    "nested-virtualization",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SupportedAdditionalProcessorFeature) -> str:
    return value


def from_ec2_query_text(text: str) -> SupportedAdditionalProcessorFeature:
    return cast(SupportedAdditionalProcessorFeature, text)


def serialize_ec2_query(
    value: SupportedAdditionalProcessorFeature,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SupportedAdditionalProcessorFeature:
    return from_ec2_query_text(el.text or "")
