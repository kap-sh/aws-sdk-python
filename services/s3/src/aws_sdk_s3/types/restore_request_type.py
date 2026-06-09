"""Generated from Smithy shape ``com.amazonaws.s3#RestoreRequestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

RestoreRequestType: TypeAlias = Literal["SELECT",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("SELECT",))


def to_xml_text(value: RestoreRequestType) -> str:
    return value


def from_xml_text(text: str) -> RestoreRequestType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RestoreRequestType value: {text!r}")
    return cast(RestoreRequestType, text)


def serialize_xml(value: RestoreRequestType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RestoreRequestType:
    return from_xml_text(el.text or "")
