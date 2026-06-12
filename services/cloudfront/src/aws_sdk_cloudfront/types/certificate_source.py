"""Generated from Smithy shape ``com.amazonaws.cloudfront#CertificateSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

CertificateSource: TypeAlias = Literal[
    "cloudfront",
    "iam",
    "acm",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cloudfront",
        "iam",
        "acm",
    )
)


def to_xml_text(value: CertificateSource) -> str:
    return value


def from_xml_text(text: str) -> CertificateSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CertificateSource value: {text!r}")
    return cast(CertificateSource, text)


def serialize_xml(value: CertificateSource, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CertificateSource:
    return from_xml_text(el.text or "")
