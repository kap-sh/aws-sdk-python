"""Generated from Smithy shape ``com.amazonaws.cloudfront#SslProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

SslProtocol: TypeAlias = Literal[
    "SSLv3",
    "TLSv1",
    "TLSv1.1",
    "TLSv1.2",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSLv3",
        "TLSv1",
        "TLSv1.1",
        "TLSv1.2",
    )
)


def to_xml_text(value: SslProtocol) -> str:
    return value


def from_xml_text(text: str) -> SslProtocol:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SslProtocol value: {text!r}")
    return cast(SslProtocol, text)


def serialize_xml(value: SslProtocol, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SslProtocol:
    return from_xml_text(el.text or "")
