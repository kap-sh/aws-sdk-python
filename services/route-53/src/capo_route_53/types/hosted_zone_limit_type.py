"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneLimitType``."""

from typing import Literal, TypeAlias, cast

from capo_route_53._protocol.xml import Element, SubElement

HostedZoneLimitType: TypeAlias = Literal[
    "MAX_RRSETS_BY_ZONE",
    "MAX_VPCS_ASSOCIATED_BY_ZONE",
]


# --- restXml ser/de ---
def to_xml_text(value: HostedZoneLimitType) -> str:
    return value


def from_xml_text(text: str) -> HostedZoneLimitType:
    return cast(HostedZoneLimitType, text)


def serialize_xml(value: HostedZoneLimitType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> HostedZoneLimitType:
    return from_xml_text(el.text or "")
