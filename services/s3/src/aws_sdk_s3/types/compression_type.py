"""Generated from Smithy shape ``com.amazonaws.s3#CompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

CompressionType: TypeAlias = Literal[
    "NONE",
    "GZIP",
    "BZIP2",
]


# --- restXml ser/de ---
def to_xml_text(value: CompressionType) -> str:
    return value


def from_xml_text(text: str) -> CompressionType:
    return cast(CompressionType, text)


def serialize_xml(value: CompressionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CompressionType:
    return from_xml_text(el.text or "")
