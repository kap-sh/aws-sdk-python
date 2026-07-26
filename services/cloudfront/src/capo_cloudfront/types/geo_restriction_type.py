"""Generated from Smithy shape ``com.amazonaws.cloudfront#GeoRestrictionType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

GeoRestrictionType: TypeAlias = Literal[
    "blacklist",
    "whitelist",
    "none",
]


# --- restXml ser/de ---
def to_xml_text(value: GeoRestrictionType) -> str:
    return value


def from_xml_text(text: str) -> GeoRestrictionType:
    return cast(GeoRestrictionType, text)


def serialize_xml(value: GeoRestrictionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> GeoRestrictionType:
    return from_xml_text(el.text or "")
