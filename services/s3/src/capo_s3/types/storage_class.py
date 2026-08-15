"""Generated from Smithy shape ``com.amazonaws.s3#StorageClass``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

StorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "GLACIER",
    "DEEP_ARCHIVE",
    "OUTPOSTS",
    "GLACIER_IR",
    "SNOW",
    "EXPRESS_ONEZONE",
    "FSX_OPENZFS",
    "FSX_ONTAP",
    "AWS_BACKUP_WARM",
    "AWS_BACKUP_LOW_COST_WARM",
]


# --- restXml ser/de ---
def to_xml_text(value: StorageClass) -> str:
    return value


def from_xml_text(text: str) -> StorageClass:
    return cast(StorageClass, text)


def serialize_xml(value: StorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> StorageClass:
    return from_xml_text(el.text or "")
