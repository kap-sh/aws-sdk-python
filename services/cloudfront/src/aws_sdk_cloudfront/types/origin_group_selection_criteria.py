"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroupSelectionCriteria``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

OriginGroupSelectionCriteria: TypeAlias = Literal[
    "default",
    "media-quality-based",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginGroupSelectionCriteria) -> str:
    return value


def from_xml_text(text: str) -> OriginGroupSelectionCriteria:
    return cast(OriginGroupSelectionCriteria, text)


def serialize_xml(
    value: OriginGroupSelectionCriteria, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginGroupSelectionCriteria:
    return from_xml_text(el.text or "")
