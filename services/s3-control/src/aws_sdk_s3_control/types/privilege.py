"""Generated from Smithy shape ``com.amazonaws.s3control#Privilege``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

Privilege: TypeAlias = Literal[
    "Minimal",
    "Default",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Minimal",
        "Default",
    )
)


def to_xml_text(value: Privilege) -> str:
    return value


def from_xml_text(text: str) -> Privilege:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Privilege value: {text!r}")
    return cast(Privilege, text)


def serialize_xml(value: Privilege, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Privilege:
    return from_xml_text(el.text or "")
