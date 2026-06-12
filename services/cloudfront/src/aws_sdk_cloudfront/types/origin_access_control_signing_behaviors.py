"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlSigningBehaviors``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginAccessControlSigningBehaviors: TypeAlias = Literal[
    "never",
    "always",
    "no-override",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "never",
        "always",
        "no-override",
    )
)


def to_xml_text(value: OriginAccessControlSigningBehaviors) -> str:
    return value


def from_xml_text(text: str) -> OriginAccessControlSigningBehaviors:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OriginAccessControlSigningBehaviors value: {text!r}"
        )
    return cast(OriginAccessControlSigningBehaviors, text)


def serialize_xml(
    value: OriginAccessControlSigningBehaviors, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginAccessControlSigningBehaviors:
    return from_xml_text(el.text or "")
