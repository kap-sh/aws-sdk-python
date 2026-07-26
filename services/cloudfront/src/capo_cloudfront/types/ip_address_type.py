"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dualstack",
]


# --- restXml ser/de ---
def to_xml_text(value: IpAddressType) -> str:
    return value


def from_xml_text(text: str) -> IpAddressType:
    return cast(IpAddressType, text)


def serialize_xml(value: IpAddressType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IpAddressType:
    return from_xml_text(el.text or "")
