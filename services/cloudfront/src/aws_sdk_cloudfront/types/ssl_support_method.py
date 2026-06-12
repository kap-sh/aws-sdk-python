"""Generated from Smithy shape ``com.amazonaws.cloudfront#SSLSupportMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

SSLSupportMethod: TypeAlias = Literal[
    "sni-only",
    "vip",
    "static-ip",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sni-only",
        "vip",
        "static-ip",
    )
)


def to_xml_text(value: SSLSupportMethod) -> str:
    return value


def from_xml_text(text: str) -> SSLSupportMethod:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SSLSupportMethod value: {text!r}")
    return cast(SSLSupportMethod, text)


def serialize_xml(value: SSLSupportMethod, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SSLSupportMethod:
    return from_xml_text(el.text or "")
