"""Generated from Smithy shape ``com.amazonaws.s3control#ExpirationStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

ExpirationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: ExpirationStatus) -> str:
    return value


def from_xml_text(text: str) -> ExpirationStatus:
    return cast(ExpirationStatus, text)


def serialize_xml(value: ExpirationStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ExpirationStatus:
    return from_xml_text(el.text or "")
