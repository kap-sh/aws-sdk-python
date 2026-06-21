"""Generated from Smithy shape ``com.amazonaws.cloudfront#DnsConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

DnsConfigurationStatus: TypeAlias = Literal[
    "valid-configuration",
    "invalid-configuration",
    "unknown-configuration",
]


# --- restXml ser/de ---
def to_xml_text(value: DnsConfigurationStatus) -> str:
    return value


def from_xml_text(text: str) -> DnsConfigurationStatus:
    return cast(DnsConfigurationStatus, text)


def serialize_xml(value: DnsConfigurationStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DnsConfigurationStatus:
    return from_xml_text(el.text or "")
