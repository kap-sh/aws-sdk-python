"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement

HealthCheckRegion: TypeAlias = Literal[
    "us-east-1",
    "us-west-1",
    "us-west-2",
    "eu-west-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "sa-east-1",
]


# --- restXml ser/de ---
def to_xml_text(value: HealthCheckRegion) -> str:
    return value


def from_xml_text(text: str) -> HealthCheckRegion:
    return cast(HealthCheckRegion, text)


def serialize_xml(value: HealthCheckRegion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HealthCheckRegion:
    return from_xml_text(el.text or "")
