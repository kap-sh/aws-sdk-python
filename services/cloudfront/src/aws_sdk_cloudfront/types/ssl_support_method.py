"""Generated from Smithy shape ``com.amazonaws.cloudfront#SSLSupportMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

SSLSupportMethod: TypeAlias = Literal[
    "sni-only",
    "vip",
    "static-ip",
]


# --- restXml ser/de ---
def to_xml_text(value: SSLSupportMethod) -> str:
    return value


def from_xml_text(text: str) -> SSLSupportMethod:
    return cast(SSLSupportMethod, text)


def serialize_xml(value: SSLSupportMethod, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SSLSupportMethod:
    return from_xml_text(el.text or "")
