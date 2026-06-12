"""Generated from Smithy shape ``com.amazonaws.cloudfront#PriceClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

PriceClass: TypeAlias = Literal[
    "PriceClass_100",
    "PriceClass_200",
    "PriceClass_All",
    "None",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PriceClass_100",
        "PriceClass_200",
        "PriceClass_All",
        "None",
    )
)


def to_xml_text(value: PriceClass) -> str:
    return value


def from_xml_text(text: str) -> PriceClass:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PriceClass value: {text!r}")
    return cast(PriceClass, text)


def serialize_xml(value: PriceClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> PriceClass:
    return from_xml_text(el.text or "")
