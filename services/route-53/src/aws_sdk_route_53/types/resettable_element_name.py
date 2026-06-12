"""Generated from Smithy shape ``com.amazonaws.route53#ResettableElementName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

ResettableElementName: TypeAlias = Literal[
    "FullyQualifiedDomainName",
    "Regions",
    "ResourcePath",
    "ChildHealthChecks",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FullyQualifiedDomainName",
        "Regions",
        "ResourcePath",
        "ChildHealthChecks",
    )
)


def to_xml_text(value: ResettableElementName) -> str:
    return value


def from_xml_text(text: str) -> ResettableElementName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ResettableElementName value: {text!r}")
    return cast(ResettableElementName, text)


def serialize_xml(value: ResettableElementName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ResettableElementName:
    return from_xml_text(el.text or "")
