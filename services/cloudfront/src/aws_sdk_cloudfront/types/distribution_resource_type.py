"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

DistributionResourceType: TypeAlias = Literal[
    "distribution",
    "distribution-tenant",
]


# --- restXml ser/de ---
def to_xml_text(value: DistributionResourceType) -> str:
    return value


def from_xml_text(text: str) -> DistributionResourceType:
    return cast(DistributionResourceType, text)


def serialize_xml(value: DistributionResourceType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DistributionResourceType:
    return from_xml_text(el.text or "")
