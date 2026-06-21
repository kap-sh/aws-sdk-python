"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

ReplicationStorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "GLACIER",
    "DEEP_ARCHIVE",
    "OUTPOSTS",
    "GLACIER_IR",
]


# --- restXml ser/de ---
def to_xml_text(value: ReplicationStorageClass) -> str:
    return value


def from_xml_text(text: str) -> ReplicationStorageClass:
    return cast(ReplicationStorageClass, text)


def serialize_xml(value: ReplicationStorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReplicationStorageClass:
    return from_xml_text(el.text or "")
