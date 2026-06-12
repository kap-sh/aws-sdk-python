"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpamCidrStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

IpamCidrStatus: TypeAlias = Literal[
    "provisioned",
    "failed-provision",
    "provisioning",
    "deprovisioned",
    "failed-deprovision",
    "deprovisioning",
    "advertised",
    "failed-advertise",
    "advertising",
    "withdrawn",
    "failed-withdraw",
    "withdrawing",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "provisioned",
        "failed-provision",
        "provisioning",
        "deprovisioned",
        "failed-deprovision",
        "deprovisioning",
        "advertised",
        "failed-advertise",
        "advertising",
        "withdrawn",
        "failed-withdraw",
        "withdrawing",
    )
)


def to_xml_text(value: IpamCidrStatus) -> str:
    return value


def from_xml_text(text: str) -> IpamCidrStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamCidrStatus value: {text!r}")
    return cast(IpamCidrStatus, text)


def serialize_xml(value: IpamCidrStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IpamCidrStatus:
    return from_xml_text(el.text or "")
