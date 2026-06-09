"""Generated from Smithy shape ``com.amazonaws.s3#SessionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

SessionMode: TypeAlias = Literal[
    "ReadOnly",
    "ReadWrite",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ReadOnly",
        "ReadWrite",
    )
)


def to_xml_text(value: SessionMode) -> str:
    return value


def from_xml_text(text: str) -> SessionMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SessionMode value: {text!r}")
    return cast(SessionMode, text)


def serialize_xml(value: SessionMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SessionMode:
    return from_xml_text(el.text or "")
