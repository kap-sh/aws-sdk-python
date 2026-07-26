"""Generated from Smithy shape ``com.amazonaws.s3#ObjectVersionStorageClass``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ObjectVersionStorageClass: TypeAlias = Literal["STANDARD",]


# --- restXml ser/de ---
def to_xml_text(value: ObjectVersionStorageClass) -> str:
    return value


def from_xml_text(text: str) -> ObjectVersionStorageClass:
    return cast(ObjectVersionStorageClass, text)


def serialize_xml(value: ObjectVersionStorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectVersionStorageClass:
    return from_xml_text(el.text or "")
