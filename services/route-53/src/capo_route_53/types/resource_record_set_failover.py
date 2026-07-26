"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetFailover``."""

from typing import Literal, TypeAlias, cast

from capo_route_53._protocol.xml import Element, SubElement

ResourceRecordSetFailover: TypeAlias = Literal[
    "PRIMARY",
    "SECONDARY",
]


# --- restXml ser/de ---
def to_xml_text(value: ResourceRecordSetFailover) -> str:
    return value


def from_xml_text(text: str) -> ResourceRecordSetFailover:
    return cast(ResourceRecordSetFailover, text)


def serialize_xml(value: ResourceRecordSetFailover, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ResourceRecordSetFailover:
    return from_xml_text(el.text or "")
