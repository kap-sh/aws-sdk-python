"""Generated from Smithy shape ``com.amazonaws.s3#BucketLogsPermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

BucketLogsPermission: TypeAlias = Literal[
    "FULL_CONTROL",
    "READ",
    "WRITE",
]


# --- restXml ser/de ---
def to_xml_text(value: BucketLogsPermission) -> str:
    return value


def from_xml_text(text: str) -> BucketLogsPermission:
    return cast(BucketLogsPermission, text)


def serialize_xml(value: BucketLogsPermission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketLogsPermission:
    return from_xml_text(el.text or "")
