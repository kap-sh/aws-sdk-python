"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dualstack",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
        "dualstack",
    )
)


def to_xml_text(value: IpAddressType) -> str:
    return value


def from_xml_text(text: str) -> IpAddressType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {text!r}")
    return cast(IpAddressType, text)


def serialize_xml(value: IpAddressType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IpAddressType:
    return from_xml_text(el.text or "")
