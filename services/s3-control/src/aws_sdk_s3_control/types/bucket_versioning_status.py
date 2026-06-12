"""Generated from Smithy shape ``com.amazonaws.s3control#BucketVersioningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

BucketVersioningStatus: TypeAlias = Literal[
    "Enabled",
    "Suspended",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Suspended",
    )
)


def to_xml_text(value: BucketVersioningStatus) -> str:
    return value


def from_xml_text(text: str) -> BucketVersioningStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketVersioningStatus value: {text!r}")
    return cast(BucketVersioningStatus, text)


def serialize_xml(value: BucketVersioningStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketVersioningStatus:
    return from_xml_text(el.text or "")
