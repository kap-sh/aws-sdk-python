"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlSigningProtocols``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

OriginAccessControlSigningProtocols: TypeAlias = Literal["sigv4",]


# --- restXml ser/de ---
def to_xml_text(value: OriginAccessControlSigningProtocols) -> str:
    return value


def from_xml_text(text: str) -> OriginAccessControlSigningProtocols:
    return cast(OriginAccessControlSigningProtocols, text)


def serialize_xml(
    value: OriginAccessControlSigningProtocols, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginAccessControlSigningProtocols:
    return from_xml_text(el.text or "")
