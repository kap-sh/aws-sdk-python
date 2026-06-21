"""Generated from Smithy shape ``com.amazonaws.s3#FileHeaderInfo``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

FileHeaderInfo: TypeAlias = Literal[
    "USE",
    "IGNORE",
    "NONE",
]


# --- restXml ser/de ---
def to_xml_text(value: FileHeaderInfo) -> str:
    return value


def from_xml_text(text: str) -> FileHeaderInfo:
    return cast(FileHeaderInfo, text)


def serialize_xml(value: FileHeaderInfo, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FileHeaderInfo:
    return from_xml_text(el.text or "")
