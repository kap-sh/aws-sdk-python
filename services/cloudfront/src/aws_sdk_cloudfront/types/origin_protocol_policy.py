"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginProtocolPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

OriginProtocolPolicy: TypeAlias = Literal[
    "http-only",
    "match-viewer",
    "https-only",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginProtocolPolicy) -> str:
    return value


def from_xml_text(text: str) -> OriginProtocolPolicy:
    return cast(OriginProtocolPolicy, text)


def serialize_xml(value: OriginProtocolPolicy, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginProtocolPolicy:
    return from_xml_text(el.text or "")
