"""Generated from Smithy shape ``com.amazonaws.route53#AcceleratedRecoveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement

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
def to_xml_text(value: AcceleratedRecoveryStatus) -> str:
    return value


def from_xml_text(text: str) -> AcceleratedRecoveryStatus:
    return cast(AcceleratedRecoveryStatus, text)


def serialize_xml(value: AcceleratedRecoveryStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AcceleratedRecoveryStatus:
    return from_xml_text(el.text or "")
