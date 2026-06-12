"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

DomainStatus: TypeAlias = Literal[
    "active",
    "inactive",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "inactive",
    )
)


def to_xml_text(value: DomainStatus) -> str:
    return value


def from_xml_text(text: str) -> DomainStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DomainStatus value: {text!r}")
    return cast(DomainStatus, text)


def serialize_xml(value: DomainStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DomainStatus:
    return from_xml_text(el.text or "")
