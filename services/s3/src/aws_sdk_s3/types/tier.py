"""Generated from Smithy shape ``com.amazonaws.s3#Tier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

Tier: TypeAlias = Literal[
    "Standard",
    "Bulk",
    "Expedited",
]


# --- restXml ser/de ---
def to_xml_text(value: Tier) -> str:
    return value


def from_xml_text(text: str) -> Tier:
    return cast(Tier, text)


def serialize_xml(value: Tier, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Tier:
    return from_xml_text(el.text or "")
