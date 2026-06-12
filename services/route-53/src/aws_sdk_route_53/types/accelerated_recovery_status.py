"""Generated from Smithy shape ``com.amazonaws.route53#AcceleratedRecoveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

AcceleratedRecoveryStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLE_FAILED",
    "ENABLING_HOSTED_ZONE_LOCKED",
    "ENABLED",
    "DISABLING",
    "DISABLE_FAILED",
    "DISABLED",
    "DISABLING_HOSTED_ZONE_LOCKED",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLE_FAILED",
        "ENABLING_HOSTED_ZONE_LOCKED",
        "ENABLED",
        "DISABLING",
        "DISABLE_FAILED",
        "DISABLED",
        "DISABLING_HOSTED_ZONE_LOCKED",
    )
)


def to_xml_text(value: AcceleratedRecoveryStatus) -> str:
    return value


def from_xml_text(text: str) -> AcceleratedRecoveryStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AcceleratedRecoveryStatus value: {text!r}")
    return cast(AcceleratedRecoveryStatus, text)


def serialize_xml(value: AcceleratedRecoveryStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AcceleratedRecoveryStatus:
    return from_xml_text(el.text or "")
