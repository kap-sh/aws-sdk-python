"""Generated from Smithy shape ``com.amazonaws.s3#SessionMode``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

SessionMode: TypeAlias = Literal[
    "ReadOnly",
    "ReadWrite",
]


# --- restXml ser/de ---
def to_xml_text(value: SessionMode) -> str:
    return value


def from_xml_text(text: str) -> SessionMode:
    return cast(SessionMode, text)


def serialize_xml(value: SessionMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SessionMode:
    return from_xml_text(el.text or "")
