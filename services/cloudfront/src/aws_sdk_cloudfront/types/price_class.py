"""Generated from Smithy shape ``com.amazonaws.cloudfront#PriceClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

PriceClass: TypeAlias = Literal[
    "PriceClass_100",
    "PriceClass_200",
    "PriceClass_All",
    "None",
]


# --- restXml ser/de ---
def to_xml_text(value: PriceClass) -> str:
    return value


def from_xml_text(text: str) -> PriceClass:
    return cast(PriceClass, text)


def serialize_xml(value: PriceClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> PriceClass:
    return from_xml_text(el.text or "")
