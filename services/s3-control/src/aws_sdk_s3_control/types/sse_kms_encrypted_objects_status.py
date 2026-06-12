"""Generated from Smithy shape ``com.amazonaws.s3control#SseKmsEncryptedObjectsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

SseKmsEncryptedObjectsStatus: TypeAlias = Literal[
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


def to_xml_text(value: SseKmsEncryptedObjectsStatus) -> str:
    return value


def from_xml_text(text: str) -> SseKmsEncryptedObjectsStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown SseKmsEncryptedObjectsStatus value: {text!r}"
        )
    return cast(SseKmsEncryptedObjectsStatus, text)


def serialize_xml(
    value: SseKmsEncryptedObjectsStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SseKmsEncryptedObjectsStatus:
    return from_xml_text(el.text or "")
