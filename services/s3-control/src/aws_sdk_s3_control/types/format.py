"""Generated from Smithy shape ``com.amazonaws.s3control#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

Format: TypeAlias = Literal[
    "CSV",
    "Parquet",
]


# --- restXml ser/de ---
def to_xml_text(value: Format) -> str:
    return value


def from_xml_text(text: str) -> Format:
    return cast(Format, text)


def serialize_xml(value: Format, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Format:
    return from_xml_text(el.text or "")
