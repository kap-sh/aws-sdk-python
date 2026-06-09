"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringAccessTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

IntelligentTieringAccessTier: TypeAlias = Literal[
    "ARCHIVE_ACCESS",
    "DEEP_ARCHIVE_ACCESS",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARCHIVE_ACCESS",
        "DEEP_ARCHIVE_ACCESS",
    )
)


def to_xml_text(value: IntelligentTieringAccessTier) -> str:
    return value


def from_xml_text(text: str) -> IntelligentTieringAccessTier:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown IntelligentTieringAccessTier value: {text!r}"
        )
    return cast(IntelligentTieringAccessTier, text)


def serialize_xml(
    value: IntelligentTieringAccessTier, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IntelligentTieringAccessTier:
    return from_xml_text(el.text or "")
