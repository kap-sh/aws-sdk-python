"""Generated from Smithy shape ``com.amazonaws.s3#ChecksumType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ChecksumType: TypeAlias = Literal[
    "COMPOSITE",
    "FULL_OBJECT",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPOSITE",
        "FULL_OBJECT",
    )
)


def to_xml_text(value: ChecksumType) -> str:
    return value


def from_xml_text(text: str) -> ChecksumType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChecksumType value: {text!r}")
    return cast(ChecksumType, text)


def serialize_xml(value: ChecksumType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChecksumType:
    return from_xml_text(el.text or "")
