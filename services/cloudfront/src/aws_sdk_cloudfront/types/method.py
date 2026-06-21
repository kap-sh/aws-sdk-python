"""Generated from Smithy shape ``com.amazonaws.cloudfront#Method``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

Method: TypeAlias = Literal[
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "PATCH",
    "OPTIONS",
    "DELETE",
]


# --- restXml ser/de ---
def to_xml_text(value: Method) -> str:
    return value


def from_xml_text(text: str) -> Method:
    return cast(Method, text)


def serialize_xml(value: Method, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Method:
    return from_xml_text(el.text or "")
