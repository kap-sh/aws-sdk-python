"""Generated from Smithy shape ``com.amazonaws.s3#MFADelete``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

MFADelete: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_xml_text(value: MFADelete) -> str:
    return value


def from_xml_text(text: str) -> MFADelete:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MFADelete value: {text!r}")
    return cast(MFADelete, text)


def serialize_xml(value: MFADelete, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MFADelete:
    return from_xml_text(el.text or "")
