"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginProtocolPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginProtocolPolicy: TypeAlias = Literal[
    "http-only",
    "match-viewer",
    "https-only",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "http-only",
        "match-viewer",
        "https-only",
    )
)


def to_xml_text(value: OriginProtocolPolicy) -> str:
    return value


def from_xml_text(text: str) -> OriginProtocolPolicy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OriginProtocolPolicy value: {text!r}")
    return cast(OriginProtocolPolicy, text)


def serialize_xml(value: OriginProtocolPolicy, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginProtocolPolicy:
    return from_xml_text(el.text or "")
