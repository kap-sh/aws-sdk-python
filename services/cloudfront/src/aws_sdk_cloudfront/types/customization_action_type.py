"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomizationActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

CustomizationActionType: TypeAlias = Literal[
    "override",
    "disable",
]


# --- restXml ser/de ---
def to_xml_text(value: CustomizationActionType) -> str:
    return value


def from_xml_text(text: str) -> CustomizationActionType:
    return cast(CustomizationActionType, text)


def serialize_xml(value: CustomizationActionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CustomizationActionType:
    return from_xml_text(el.text or "")
