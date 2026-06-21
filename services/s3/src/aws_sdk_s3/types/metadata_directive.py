"""Generated from Smithy shape ``com.amazonaws.s3#MetadataDirective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

MetadataDirective: TypeAlias = Literal[
    "COPY",
    "REPLACE",
]


# --- restXml ser/de ---
def to_xml_text(value: MetadataDirective) -> str:
    return value


def from_xml_text(text: str) -> MetadataDirective:
    return cast(MetadataDirective, text)


def serialize_xml(value: MetadataDirective, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MetadataDirective:
    return from_xml_text(el.text or "")
