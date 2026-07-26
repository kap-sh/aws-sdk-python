"""Generated from Smithy shape ``com.amazonaws.s3#Permission``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

Permission: TypeAlias = Literal[
    "FULL_CONTROL",
    "WRITE",
    "WRITE_ACP",
    "READ",
    "READ_ACP",
]


# --- restXml ser/de ---
def to_xml_text(value: Permission) -> str:
    return value


def from_xml_text(text: str) -> Permission:
    return cast(Permission, text)


def serialize_xml(value: Permission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Permission:
    return from_xml_text(el.text or "")
