"""Generated from Smithy shape ``com.amazonaws.s3#ChecksumMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ChecksumMode: TypeAlias = Literal["ENABLED",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("ENABLED",))


def to_xml_text(value: ChecksumMode) -> str:
    return value


def from_xml_text(text: str) -> ChecksumMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChecksumMode value: {text!r}")
    return cast(ChecksumMode, text)


def serialize_xml(value: ChecksumMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChecksumMode:
    return from_xml_text(el.text or "")
