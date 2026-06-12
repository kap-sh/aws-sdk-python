"""Generated from Smithy shape ``com.amazonaws.s3control#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

Permission: TypeAlias = Literal[
    "READ",
    "WRITE",
    "READWRITE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "WRITE",
        "READWRITE",
    )
)


def to_xml_text(value: Permission) -> str:
    return value


def from_xml_text(text: str) -> Permission:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {text!r}")
    return cast(Permission, text)


def serialize_xml(value: Permission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Permission:
    return from_xml_text(el.text or "")
