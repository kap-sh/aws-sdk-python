"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneType``."""

from typing import Literal, TypeAlias, cast

from capo_route_53._protocol.xml import Element, SubElement

HostedZoneType: TypeAlias = Literal["PrivateHostedZone",]


# --- restXml ser/de ---
def to_xml_text(value: HostedZoneType) -> str:
    return value


def from_xml_text(text: str) -> HostedZoneType:
    return cast(HostedZoneType, text)


def serialize_xml(value: HostedZoneType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HostedZoneType:
    return from_xml_text(el.text or "")
