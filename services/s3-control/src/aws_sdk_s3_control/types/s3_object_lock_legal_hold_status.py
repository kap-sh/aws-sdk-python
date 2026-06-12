"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockLegalHoldStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3ObjectLockLegalHoldStatus: TypeAlias = Literal[
    "OFF",
    "ON",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "ON",
    )
)


def to_xml_text(value: S3ObjectLockLegalHoldStatus) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockLegalHoldStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown S3ObjectLockLegalHoldStatus value: {text!r}"
        )
    return cast(S3ObjectLockLegalHoldStatus, text)


def serialize_xml(
    value: S3ObjectLockLegalHoldStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockLegalHoldStatus:
    return from_xml_text(el.text or "")
