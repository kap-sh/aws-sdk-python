"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroupSelectionCriteria``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginGroupSelectionCriteria: TypeAlias = Literal[
    "default",
    "media-quality-based",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "media-quality-based",
    )
)


def to_xml_text(value: OriginGroupSelectionCriteria) -> str:
    return value


def from_xml_text(text: str) -> OriginGroupSelectionCriteria:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OriginGroupSelectionCriteria value: {text!r}"
        )
    return cast(OriginGroupSelectionCriteria, text)


def serialize_xml(
    value: OriginGroupSelectionCriteria, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginGroupSelectionCriteria:
    return from_xml_text(el.text or "")
