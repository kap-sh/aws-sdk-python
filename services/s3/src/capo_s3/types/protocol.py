"""Generated from Smithy shape ``com.amazonaws.s3#Protocol``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

Protocol: TypeAlias = Literal[
    "http",
    "https",
]


# --- restXml ser/de ---
def to_xml_text(value: Protocol) -> str:
    return value


def from_xml_text(text: str) -> Protocol:
    return cast(Protocol, text)


def serialize_xml(value: Protocol, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Protocol:
    return from_xml_text(el.text or "")
