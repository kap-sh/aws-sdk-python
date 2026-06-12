"""Generated from Smithy shape ``com.amazonaws.cloudfront#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

EventType: TypeAlias = Literal[
    "viewer-request",
    "viewer-response",
    "origin-request",
    "origin-response",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "viewer-request",
        "viewer-response",
        "origin-request",
        "origin-response",
    )
)


def to_xml_text(value: EventType) -> str:
    return value


def from_xml_text(text: str) -> EventType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {text!r}")
    return cast(EventType, text)


def serialize_xml(value: EventType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> EventType:
    return from_xml_text(el.text or "")
