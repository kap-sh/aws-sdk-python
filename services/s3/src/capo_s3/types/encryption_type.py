"""Generated from Smithy shape ``com.amazonaws.s3#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

EncryptionType: TypeAlias = Literal[
    "NONE",
    "SSE-C",
]


# --- restXml ser/de ---
def to_xml_text(value: EncryptionType) -> str:
    return value


def from_xml_text(text: str) -> EncryptionType:
    return cast(EncryptionType, text)


def serialize_xml(value: EncryptionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> EncryptionType:
    return from_xml_text(el.text or "")
