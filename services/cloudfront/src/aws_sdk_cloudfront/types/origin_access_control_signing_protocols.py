"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlSigningProtocols``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginAccessControlSigningProtocols: TypeAlias = Literal["sigv4",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("sigv4",))


def to_xml_text(value: OriginAccessControlSigningProtocols) -> str:
    return value


def from_xml_text(text: str) -> OriginAccessControlSigningProtocols:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OriginAccessControlSigningProtocols value: {text!r}"
        )
    return cast(OriginAccessControlSigningProtocols, text)


def serialize_xml(
    value: OriginAccessControlSigningProtocols, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginAccessControlSigningProtocols:
    return from_xml_text(el.text or "")
