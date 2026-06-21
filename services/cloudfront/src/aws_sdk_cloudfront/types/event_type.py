"""Generated from Smithy shape ``com.amazonaws.cloudfront#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

EventType: TypeAlias = Literal[
    "viewer-request",
    "viewer-response",
    "origin-request",
    "origin-response",
]


# --- restXml ser/de ---
def to_xml_text(value: EventType) -> str:
    return value


def from_xml_text(text: str) -> EventType:
    return cast(EventType, text)


def serialize_xml(value: EventType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> EventType:
    return from_xml_text(el.text or "")
