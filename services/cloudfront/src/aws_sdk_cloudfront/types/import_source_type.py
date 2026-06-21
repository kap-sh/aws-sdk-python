"""Generated from Smithy shape ``com.amazonaws.cloudfront#ImportSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

ImportSourceType: TypeAlias = Literal["S3",]


# --- restXml ser/de ---
def to_xml_text(value: ImportSourceType) -> str:
    return value


def from_xml_text(text: str) -> ImportSourceType:
    return cast(ImportSourceType, text)


def serialize_xml(value: ImportSourceType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ImportSourceType:
    return from_xml_text(el.text or "")
