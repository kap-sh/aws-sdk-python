"""Generated from Smithy shape ``com.amazonaws.route53#RRType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

RRType: TypeAlias = Literal[
    "SOA",
    "A",
    "TXT",
    "NS",
    "CNAME",
    "MX",
    "NAPTR",
    "PTR",
    "SRV",
    "SPF",
    "AAAA",
    "CAA",
    "DS",
    "TLSA",
    "SSHFP",
    "SVCB",
    "HTTPS",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOA",
        "A",
        "TXT",
        "NS",
        "CNAME",
        "MX",
        "NAPTR",
        "PTR",
        "SRV",
        "SPF",
        "AAAA",
        "CAA",
        "DS",
        "TLSA",
        "SSHFP",
        "SVCB",
        "HTTPS",
    )
)


def to_xml_text(value: RRType) -> str:
    return value


def from_xml_text(text: str) -> RRType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RRType value: {text!r}")
    return cast(RRType, text)


def serialize_xml(value: RRType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RRType:
    return from_xml_text(el.text or "")
