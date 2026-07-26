"""Generated from Smithy shape ``com.amazonaws.s3control#Privilege``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

Privilege: TypeAlias = Literal[
    "Minimal",
    "Default",
]


# --- restXml ser/de ---
def to_xml_text(value: Privilege) -> str:
    return value


def from_xml_text(text: str) -> Privilege:
    return cast(Privilege, text)


def serialize_xml(value: Privilege, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Privilege:
    return from_xml_text(el.text or "")
