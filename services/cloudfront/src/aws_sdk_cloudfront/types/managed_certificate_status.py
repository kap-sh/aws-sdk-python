"""Generated from Smithy shape ``com.amazonaws.cloudfront#ManagedCertificateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

ManagedCertificateStatus: TypeAlias = Literal[
    "pending-validation",
    "issued",
    "inactive",
    "expired",
    "validation-timed-out",
    "revoked",
    "failed",
]


# --- restXml ser/de ---
def to_xml_text(value: ManagedCertificateStatus) -> str:
    return value


def from_xml_text(text: str) -> ManagedCertificateStatus:
    return cast(ManagedCertificateStatus, text)


def serialize_xml(value: ManagedCertificateStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ManagedCertificateStatus:
    return from_xml_text(el.text or "")
