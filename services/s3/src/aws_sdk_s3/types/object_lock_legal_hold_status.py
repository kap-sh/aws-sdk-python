"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockLegalHoldStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ObjectLockLegalHoldStatus: TypeAlias = Literal[
    "ON",
    "OFF",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON",
        "OFF",
    )
)


def to_xml_text(value: ObjectLockLegalHoldStatus) -> str:
    return value


def from_xml_text(text: str) -> ObjectLockLegalHoldStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ObjectLockLegalHoldStatus value: {text!r}")
    return cast(ObjectLockLegalHoldStatus, text)


def serialize_xml(value: ObjectLockLegalHoldStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLockLegalHoldStatus:
    return from_xml_text(el.text or "")
