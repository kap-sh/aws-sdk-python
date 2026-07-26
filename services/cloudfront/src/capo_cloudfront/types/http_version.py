"""Generated from Smithy shape ``com.amazonaws.cloudfront#HttpVersion``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

HttpVersion: TypeAlias = Literal[
    "http1.1",
    "http2",
    "http3",
    "http2and3",
]


# --- restXml ser/de ---
def to_xml_text(value: HttpVersion) -> str:
    return value


def from_xml_text(text: str) -> HttpVersion:
    return cast(HttpVersion, text)


def serialize_xml(value: HttpVersion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HttpVersion:
    return from_xml_text(el.text or "")
