"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetFailover``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

ResourceRecordSetFailover: TypeAlias = Literal[
    "PRIMARY",
    "SECONDARY",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "SECONDARY",
    )
)


def to_xml_text(value: ResourceRecordSetFailover) -> str:
    return value


def from_xml_text(text: str) -> ResourceRecordSetFailover:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ResourceRecordSetFailover value: {text!r}")
    return cast(ResourceRecordSetFailover, text)


def serialize_xml(value: ResourceRecordSetFailover, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ResourceRecordSetFailover:
    return from_xml_text(el.text or "")
