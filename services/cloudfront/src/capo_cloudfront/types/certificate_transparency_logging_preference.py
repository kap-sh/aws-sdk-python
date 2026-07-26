"""Generated from Smithy shape ``com.amazonaws.cloudfront#CertificateTransparencyLoggingPreference``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

CertificateTransparencyLoggingPreference: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: CertificateTransparencyLoggingPreference) -> str:
    return value


def from_xml_text(text: str) -> CertificateTransparencyLoggingPreference:
    return cast(CertificateTransparencyLoggingPreference, text)


def serialize_xml(
    value: CertificateTransparencyLoggingPreference, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CertificateTransparencyLoggingPreference:
    return from_xml_text(el.text or "")
