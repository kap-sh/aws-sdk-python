"""Generated from Smithy shape ``com.amazonaws.cloudfront#GeoRestrictionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

GeoRestrictionType: TypeAlias = Literal[
    "blacklist",
    "whitelist",
    "none",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "blacklist",
        "whitelist",
        "none",
    )
)


def to_xml_text(value: GeoRestrictionType) -> str:
    return value


def from_xml_text(text: str) -> GeoRestrictionType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown GeoRestrictionType value: {text!r}")
    return cast(GeoRestrictionType, text)


def serialize_xml(value: GeoRestrictionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> GeoRestrictionType:
    return from_xml_text(el.text or "")
