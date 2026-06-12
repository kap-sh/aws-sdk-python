"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

HostedZoneType: TypeAlias = Literal["PrivateHostedZone",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("PrivateHostedZone",))


def to_xml_text(value: HostedZoneType) -> str:
    return value


def from_xml_text(text: str) -> HostedZoneType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HostedZoneType value: {text!r}")
    return cast(HostedZoneType, text)


def serialize_xml(value: HostedZoneType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HostedZoneType:
    return from_xml_text(el.text or "")
