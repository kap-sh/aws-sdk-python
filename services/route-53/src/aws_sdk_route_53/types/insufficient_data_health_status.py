"""Generated from Smithy shape ``com.amazonaws.route53#InsufficientDataHealthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

InsufficientDataHealthStatus: TypeAlias = Literal[
    "Healthy",
    "Unhealthy",
    "LastKnownStatus",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Healthy",
        "Unhealthy",
        "LastKnownStatus",
    )
)


def to_xml_text(value: InsufficientDataHealthStatus) -> str:
    return value


def from_xml_text(text: str) -> InsufficientDataHealthStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InsufficientDataHealthStatus value: {text!r}"
        )
    return cast(InsufficientDataHealthStatus, text)


def serialize_xml(
    value: InsufficientDataHealthStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InsufficientDataHealthStatus:
    return from_xml_text(el.text or "")
