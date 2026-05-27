"""Generated from Smithy shape ``com.amazonaws.s3#CompressionType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

CompressionType: TypeAlias = Literal[
    "NONE",
    "GZIP",
    "BZIP2",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "GZIP",
        "BZIP2",
    )
)


def to_xml_text(value: CompressionType) -> str:
    return value


def from_xml_text(text: str) -> CompressionType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CompressionType value: {text!r}")
    return cast(CompressionType, text)


def serialize_xml(value: CompressionType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CompressionType:
    return from_xml_text(el.text or "")
