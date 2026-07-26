"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionMode``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ConnectionMode: TypeAlias = Literal[
    "direct",
    "tenant-only",
]


# --- restXml ser/de ---
def to_xml_text(value: ConnectionMode) -> str:
    return value


def from_xml_text(text: str) -> ConnectionMode:
    return cast(ConnectionMode, text)


def serialize_xml(value: ConnectionMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ConnectionMode:
    return from_xml_text(el.text or "")
