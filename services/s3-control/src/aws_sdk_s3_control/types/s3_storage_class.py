"""Generated from Smithy shape ``com.amazonaws.s3control#S3StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

S3StorageClass: TypeAlias = Literal[
    "STANDARD",
    "STANDARD_IA",
    "ONEZONE_IA",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "DEEP_ARCHIVE",
    "GLACIER_IR",
]


# --- restXml ser/de ---
def to_xml_text(value: S3StorageClass) -> str:
    return value


def from_xml_text(text: str) -> S3StorageClass:
    return cast(S3StorageClass, text)


def serialize_xml(value: S3StorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3StorageClass:
    return from_xml_text(el.text or "")
