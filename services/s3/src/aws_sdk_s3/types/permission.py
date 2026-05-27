"""Generated from Smithy shape ``com.amazonaws.s3#Permission``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

Permission: TypeAlias = Literal[
    "FULL_CONTROL",
    "WRITE",
    "WRITE_ACP",
    "READ",
    "READ_ACP",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_CONTROL",
        "WRITE",
        "WRITE_ACP",
        "READ",
        "READ_ACP",
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
