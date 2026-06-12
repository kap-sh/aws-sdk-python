"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "us-east-1",
        "us-west-1",
        "us-west-2",
        "eu-west-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "sa-east-1",
    )
)


def to_xml_text(value: HealthCheckRegion) -> str:
    return value


def from_xml_text(text: str) -> HealthCheckRegion:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HealthCheckRegion value: {text!r}")
    return cast(HealthCheckRegion, text)


def serialize_xml(value: HealthCheckRegion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HealthCheckRegion:
    return from_xml_text(el.text or "")
