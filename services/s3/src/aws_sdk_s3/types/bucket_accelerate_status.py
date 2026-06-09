"""Generated from Smithy shape ``com.amazonaws.s3#BucketAccelerateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

BucketAccelerateStatus: TypeAlias = Literal[
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


def to_xml_text(value: BucketAccelerateStatus) -> str:
    return value


def from_xml_text(text: str) -> BucketAccelerateStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketAccelerateStatus value: {text!r}")
    return cast(BucketAccelerateStatus, text)


def serialize_xml(value: BucketAccelerateStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketAccelerateStatus:
    return from_xml_text(el.text or "")
