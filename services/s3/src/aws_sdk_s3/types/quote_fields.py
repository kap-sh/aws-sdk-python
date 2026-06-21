"""Generated from Smithy shape ``com.amazonaws.s3#QuoteFields``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

QuoteFields: TypeAlias = Literal[
    "ALWAYS",
    "ASNEEDED",
]


# --- restXml ser/de ---
def to_xml_text(value: QuoteFields) -> str:
    return value


def from_xml_text(text: str) -> QuoteFields:
    return cast(QuoteFields, text)


def serialize_xml(value: QuoteFields, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> QuoteFields:
    return from_xml_text(el.text or "")
