"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement

HealthCheckType: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
    "HTTP_STR_MATCH",
    "HTTPS_STR_MATCH",
    "TCP",
    "CALCULATED",
    "CLOUDWATCH_METRIC",
    "RECOVERY_CONTROL",
]


# --- restXml ser/de ---
def to_xml_text(value: HealthCheckType) -> str:
    return value


def from_xml_text(text: str) -> HealthCheckType:
    return cast(HealthCheckType, text)


def serialize_xml(value: HealthCheckType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HealthCheckType:
    return from_xml_text(el.text or "")
