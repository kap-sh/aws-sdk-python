"""Generated from Smithy shape ``com.amazonaws.s3control#ComputeObjectChecksumType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

ComputeObjectChecksumType: TypeAlias = Literal[
    "FULL_OBJECT",
    "COMPOSITE",
]


# --- restXml ser/de ---
def to_xml_text(value: ComputeObjectChecksumType) -> str:
    return value


def from_xml_text(text: str) -> ComputeObjectChecksumType:
    return cast(ComputeObjectChecksumType, text)


def serialize_xml(value: ComputeObjectChecksumType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ComputeObjectChecksumType:
    return from_xml_text(el.text or "")
