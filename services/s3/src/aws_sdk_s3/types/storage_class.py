"""Generated from Smithy shape ``com.amazonaws.s3#StorageClass``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

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
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def to_xml_text(value: StorageClass) -> str:
    return value


def from_xml_text(text: str) -> StorageClass:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StorageClass value: {text!r}")
    return cast(StorageClass, text)


def serialize_xml(value: StorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> StorageClass:
    return from_xml_text(el.text or "")
