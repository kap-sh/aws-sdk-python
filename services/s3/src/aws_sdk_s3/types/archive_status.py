"""Generated from Smithy shape ``com.amazonaws.s3#ArchiveStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ArchiveStatus: TypeAlias = Literal[
    "ARCHIVE_ACCESS",
    "DEEP_ARCHIVE_ACCESS",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARCHIVE_ACCESS",
        "DEEP_ARCHIVE_ACCESS",
    )
)


def to_xml_text(value: ArchiveStatus) -> str:
    return value


def from_xml_text(text: str) -> ArchiveStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ArchiveStatus value: {text!r}")
    return cast(ArchiveStatus, text)


def serialize_xml(value: ArchiveStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ArchiveStatus:
    return from_xml_text(el.text or "")
