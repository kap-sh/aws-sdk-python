"""Generated from Smithy shape ``com.amazonaws.cloudfront#DnsConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

DnsConfigurationStatus: TypeAlias = Literal[
    "valid-configuration",
    "invalid-configuration",
    "unknown-configuration",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "valid-configuration",
        "invalid-configuration",
        "unknown-configuration",
    )
)


def to_xml_text(value: DnsConfigurationStatus) -> str:
    return value


def from_xml_text(text: str) -> DnsConfigurationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DnsConfigurationStatus value: {text!r}")
    return cast(DnsConfigurationStatus, text)


def serialize_xml(value: DnsConfigurationStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DnsConfigurationStatus:
    return from_xml_text(el.text or "")
