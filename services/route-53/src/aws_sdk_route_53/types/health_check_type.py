"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP",
        "HTTPS",
        "HTTP_STR_MATCH",
        "HTTPS_STR_MATCH",
        "TCP",
        "CALCULATED",
        "CLOUDWATCH_METRIC",
        "RECOVERY_CONTROL",
    )
)


def to_xml_text(value: HealthCheckType) -> str:
    return value


def from_xml_text(text: str) -> HealthCheckType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HealthCheckType value: {text!r}")
    return cast(HealthCheckType, text)


def serialize_xml(value: HealthCheckType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HealthCheckType:
    return from_xml_text(el.text or "")
