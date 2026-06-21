"""Generated from Smithy shape ``com.amazonaws.s3#ChecksumType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

ChecksumType: TypeAlias = Literal[
    "COMPOSITE",
    "FULL_OBJECT",
]


# --- restXml ser/de ---
def to_xml_text(value: ChecksumType) -> str:
    return value


def from_xml_text(text: str) -> ChecksumType:
    return cast(ChecksumType, text)


def serialize_xml(value: ChecksumType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChecksumType:
    return from_xml_text(el.text or "")
