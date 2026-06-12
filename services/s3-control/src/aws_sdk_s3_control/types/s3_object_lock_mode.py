"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3ObjectLockMode: TypeAlias = Literal[
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


def to_xml_text(value: S3ObjectLockMode) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3ObjectLockMode value: {text!r}")
    return cast(S3ObjectLockMode, text)


def serialize_xml(value: S3ObjectLockMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockMode:
    return from_xml_text(el.text or "")
