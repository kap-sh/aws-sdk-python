"""Generated from Smithy shape ``com.amazonaws.s3#BucketLogsPermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

BucketLogsPermission: TypeAlias = Literal[
    "FULL_CONTROL",
    "READ",
    "WRITE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_CONTROL",
        "READ",
        "WRITE",
    )
)


def to_xml_text(value: BucketLogsPermission) -> str:
    return value


def from_xml_text(text: str) -> BucketLogsPermission:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketLogsPermission value: {text!r}")
    return cast(BucketLogsPermission, text)


def serialize_xml(value: BucketLogsPermission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketLogsPermission:
    return from_xml_text(el.text or "")
