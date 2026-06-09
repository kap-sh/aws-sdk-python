"""Generated from Smithy shape ``com.amazonaws.s3#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "NONE",
    "SSE-C",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SSE-C",
    )
)


def to_xml_text(value: EncryptionType) -> str:
    return value


def from_xml_text(text: str) -> EncryptionType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {text!r}")
    return cast(EncryptionType, text)


def serialize_xml(value: EncryptionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> EncryptionType:
    return from_xml_text(el.text or "")
