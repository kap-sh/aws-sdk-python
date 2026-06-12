"""Generated from Smithy shape ``com.amazonaws.s3control#S3Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3Permission: TypeAlias = Literal[
    "FULL_CONTROL",
    "READ",
    "WRITE",
    "READ_ACP",
    "WRITE_ACP",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_CONTROL",
        "READ",
        "WRITE",
        "READ_ACP",
        "WRITE_ACP",
    )
)


def to_xml_text(value: S3Permission) -> str:
    return value


def from_xml_text(text: str) -> S3Permission:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3Permission value: {text!r}")
    return cast(S3Permission, text)


def serialize_xml(value: S3Permission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3Permission:
    return from_xml_text(el.text or "")
