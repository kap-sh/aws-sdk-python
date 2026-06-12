"""Generated from Smithy shape ``com.amazonaws.cloudfront#Method``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "HEAD",
        "POST",
        "PUT",
        "PATCH",
        "OPTIONS",
        "DELETE",
    )
)


def to_xml_text(value: Method) -> str:
    return value


def from_xml_text(text: str) -> Method:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Method value: {text!r}")
    return cast(Method, text)


def serialize_xml(value: Method, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Method:
    return from_xml_text(el.text or "")
