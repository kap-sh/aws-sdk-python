"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpamCidrStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

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
def to_xml_text(value: IpamCidrStatus) -> str:
    return value


def from_xml_text(text: str) -> IpamCidrStatus:
    return cast(IpamCidrStatus, text)


def serialize_xml(value: IpamCidrStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IpamCidrStatus:
    return from_xml_text(el.text or "")
