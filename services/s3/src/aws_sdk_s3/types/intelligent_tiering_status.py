"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

IntelligentTieringStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: IntelligentTieringStatus) -> str:
    return value


def from_xml_text(text: str) -> IntelligentTieringStatus:
    return cast(IntelligentTieringStatus, text)


def serialize_xml(value: IntelligentTieringStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IntelligentTieringStatus:
    return from_xml_text(el.text or "")
