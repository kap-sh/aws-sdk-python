"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

IntelligentTieringStatus: TypeAlias = Literal[
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


def to_xml_text(value: IntelligentTieringStatus) -> str:
    return value


def from_xml_text(text: str) -> IntelligentTieringStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IntelligentTieringStatus value: {text!r}")
    return cast(IntelligentTieringStatus, text)


def serialize_xml(value: IntelligentTieringStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IntelligentTieringStatus:
    return from_xml_text(el.text or "")
