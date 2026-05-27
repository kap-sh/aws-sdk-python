"""Generated from Smithy shape ``com.amazonaws.s3#BucketCannedACL``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

BucketCannedACL: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "private",
        "public-read",
        "public-read-write",
        "authenticated-read",
    )
)


def to_xml_text(value: BucketCannedACL) -> str:
    return value


def from_xml_text(text: str) -> BucketCannedACL:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketCannedACL value: {text!r}")
    return cast(BucketCannedACL, text)


def serialize_xml(value: BucketCannedACL, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketCannedACL:
    return from_xml_text(el.text or "")
