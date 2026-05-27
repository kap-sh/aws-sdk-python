"""Generated from Smithy shape ``com.amazonaws.s3#ObjectCannedACL``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

ObjectCannedACL: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "private",
        "public-read",
        "public-read-write",
        "authenticated-read",
        "aws-exec-read",
        "bucket-owner-read",
        "bucket-owner-full-control",
    )
)


def to_xml_text(value: ObjectCannedACL) -> str:
    return value


def from_xml_text(text: str) -> ObjectCannedACL:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ObjectCannedACL value: {text!r}")
    return cast(ObjectCannedACL, text)


def serialize_xml(value: ObjectCannedACL, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectCannedACL:
    return from_xml_text(el.text or "")
