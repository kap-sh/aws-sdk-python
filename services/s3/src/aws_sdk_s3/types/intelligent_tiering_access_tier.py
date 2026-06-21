"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringAccessTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

IntelligentTieringAccessTier: TypeAlias = Literal[
    "ARCHIVE_ACCESS",
    "DEEP_ARCHIVE_ACCESS",
]


# --- restXml ser/de ---
def to_xml_text(value: IntelligentTieringAccessTier) -> str:
    return value


def from_xml_text(text: str) -> IntelligentTieringAccessTier:
    return cast(IntelligentTieringAccessTier, text)


def serialize_xml(
    value: IntelligentTieringAccessTier, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IntelligentTieringAccessTier:
    return from_xml_text(el.text or "")
