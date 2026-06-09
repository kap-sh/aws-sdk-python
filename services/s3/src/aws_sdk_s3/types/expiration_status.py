"""Generated from Smithy shape ``com.amazonaws.s3#ExpirationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ExpirationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_xml_text(value: ExpirationStatus) -> str:
    return value


def from_xml_text(text: str) -> ExpirationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ExpirationStatus value: {text!r}")
    return cast(ExpirationStatus, text)


def serialize_xml(value: ExpirationStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ExpirationStatus:
    return from_xml_text(el.text or "")
