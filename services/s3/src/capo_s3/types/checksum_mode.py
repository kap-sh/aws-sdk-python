"""Generated from Smithy shape ``com.amazonaws.s3#ChecksumMode``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ChecksumMode: TypeAlias = Literal["ENABLED",]


# --- restXml ser/de ---
def to_xml_text(value: ChecksumMode) -> str:
    return value


def from_xml_text(text: str) -> ChecksumMode:
    return cast(ChecksumMode, text)


def serialize_xml(value: ChecksumMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChecksumMode:
    return from_xml_text(el.text or "")
