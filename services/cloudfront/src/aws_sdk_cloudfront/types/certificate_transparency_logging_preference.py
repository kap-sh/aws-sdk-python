"""Generated from Smithy shape ``com.amazonaws.cloudfront#CertificateTransparencyLoggingPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

CertificateTransparencyLoggingPreference: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def to_xml_text(value: CertificateTransparencyLoggingPreference) -> str:
    return value


def from_xml_text(text: str) -> CertificateTransparencyLoggingPreference:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateTransparencyLoggingPreference value: {text!r}"
        )
    return cast(CertificateTransparencyLoggingPreference, text)


def serialize_xml(
    value: CertificateTransparencyLoggingPreference, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CertificateTransparencyLoggingPreference:
    return from_xml_text(el.text or "")
