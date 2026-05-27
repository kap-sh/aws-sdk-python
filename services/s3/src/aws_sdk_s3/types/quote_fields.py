"""Generated from Smithy shape ``com.amazonaws.s3#QuoteFields``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

QuoteFields: TypeAlias = Literal[
    "ALWAYS",
    "ASNEEDED",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS",
        "ASNEEDED",
    )
)


def to_xml_text(value: QuoteFields) -> str:
    return value


def from_xml_text(text: str) -> QuoteFields:
    if text not in _VALUES:
        raise DeserializationError(f"unknown QuoteFields value: {text!r}")
    return cast(QuoteFields, text)


def serialize_xml(value: QuoteFields, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> QuoteFields:
    return from_xml_text(el.text or "")
