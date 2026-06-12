"""Generated from Smithy shape ``com.amazonaws.s3control#S3PrefixType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3PrefixType: TypeAlias = Literal["Object",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("Object",))


def to_xml_text(value: S3PrefixType) -> str:
    return value


def from_xml_text(text: str) -> S3PrefixType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3PrefixType value: {text!r}")
    return cast(S3PrefixType, text)


def serialize_xml(value: S3PrefixType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3PrefixType:
    return from_xml_text(el.text or "")
