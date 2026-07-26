"""Generated from Smithy shape ``com.amazonaws.s3#RestoreRequestType``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

RestoreRequestType: TypeAlias = Literal["SELECT",]


# --- restXml ser/de ---
def to_xml_text(value: RestoreRequestType) -> str:
    return value


def from_xml_text(text: str) -> RestoreRequestType:
    return cast(RestoreRequestType, text)


def serialize_xml(value: RestoreRequestType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RestoreRequestType:
    return from_xml_text(el.text or "")
