"""Generated from Smithy shape ``com.amazonaws.cloudfront#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

Format: TypeAlias = Literal["URLEncoded",]


# --- restXml ser/de ---
def to_xml_text(value: Format) -> str:
    return value


def from_xml_text(text: str) -> Format:
    return cast(Format, text)


def serialize_xml(value: Format, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Format:
    return from_xml_text(el.text or "")
