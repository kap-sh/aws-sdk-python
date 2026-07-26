"""Generated from Smithy shape ``com.amazonaws.s3#ObjectAttributes``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ObjectAttributes: TypeAlias = Literal[
    "ETag",
    "Checksum",
    "ObjectParts",
    "StorageClass",
    "ObjectSize",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectAttributes) -> str:
    return value


def from_xml_text(text: str) -> ObjectAttributes:
    return cast(ObjectAttributes, text)


def serialize_xml(value: ObjectAttributes, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectAttributes:
    return from_xml_text(el.text or "")
