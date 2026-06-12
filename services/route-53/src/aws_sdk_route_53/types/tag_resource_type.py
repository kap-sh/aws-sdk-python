"""Generated from Smithy shape ``com.amazonaws.route53#TagResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

TagResourceType: TypeAlias = Literal[
    "healthcheck",
    "hostedzone",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "healthcheck",
        "hostedzone",
    )
)


def to_xml_text(value: TagResourceType) -> str:
    return value


def from_xml_text(text: str) -> TagResourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TagResourceType value: {text!r}")
    return cast(TagResourceType, text)


def serialize_xml(value: TagResourceType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TagResourceType:
    return from_xml_text(el.text or "")
