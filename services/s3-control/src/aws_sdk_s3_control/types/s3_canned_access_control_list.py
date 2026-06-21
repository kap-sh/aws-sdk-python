"""Generated from Smithy shape ``com.amazonaws.s3control#S3CannedAccessControlList``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

S3CannedAccessControlList: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "aws-exec-read",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
]


# --- restXml ser/de ---
def to_xml_text(value: S3CannedAccessControlList) -> str:
    return value


def from_xml_text(text: str) -> S3CannedAccessControlList:
    return cast(S3CannedAccessControlList, text)


def serialize_xml(value: S3CannedAccessControlList, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3CannedAccessControlList:
    return from_xml_text(el.text or "")
