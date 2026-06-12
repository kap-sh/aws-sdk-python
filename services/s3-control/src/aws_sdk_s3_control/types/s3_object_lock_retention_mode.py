"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockRetentionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3ObjectLockRetentionMode: TypeAlias = Literal[
    "COMPLIANCE",
    "GOVERNANCE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLIANCE",
        "GOVERNANCE",
    )
)


def to_xml_text(value: S3ObjectLockRetentionMode) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockRetentionMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3ObjectLockRetentionMode value: {text!r}")
    return cast(S3ObjectLockRetentionMode, text)


def serialize_xml(value: S3ObjectLockRetentionMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockRetentionMode:
    return from_xml_text(el.text or "")
