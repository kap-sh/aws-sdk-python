"""Generated from Smithy shape ``com.amazonaws.s3#ObjectStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

ObjectStorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "GLACIER",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "DEEP_ARCHIVE",
    "OUTPOSTS",
    "GLACIER_IR",
    "SNOW",
    "EXPRESS_ONEZONE",
    "FSX_OPENZFS",
    "FSX_ONTAP",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectStorageClass) -> str:
    return value


def from_xml_text(text: str) -> ObjectStorageClass:
    return cast(ObjectStorageClass, text)


def serialize_xml(value: ObjectStorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectStorageClass:
    return from_xml_text(el.text or "")
