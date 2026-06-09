"""Generated from Smithy shape ``com.amazonaws.s3#BucketAbacStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

BucketAbacStatus: TypeAlias = Literal[
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


def to_xml_text(value: BucketAbacStatus) -> str:
    return value


def from_xml_text(text: str) -> BucketAbacStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketAbacStatus value: {text!r}")
    return cast(BucketAbacStatus, text)


def serialize_xml(value: BucketAbacStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketAbacStatus:
    return from_xml_text(el.text or "")
