"""Generated from Smithy shape ``com.amazonaws.cloudfront#ValidationTokenHost``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

ValidationTokenHost: TypeAlias = Literal[
    "cloudfront",
    "self-hosted",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cloudfront",
        "self-hosted",
    )
)


def to_xml_text(value: ValidationTokenHost) -> str:
    return value


def from_xml_text(text: str) -> ValidationTokenHost:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ValidationTokenHost value: {text!r}")
    return cast(ValidationTokenHost, text)


def serialize_xml(value: ValidationTokenHost, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ValidationTokenHost:
    return from_xml_text(el.text or "")
