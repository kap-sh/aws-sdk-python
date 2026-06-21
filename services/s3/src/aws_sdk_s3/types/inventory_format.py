"""Generated from Smithy shape ``com.amazonaws.s3#InventoryFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

InventoryFormat: TypeAlias = Literal[
    "CSV",
    "ORC",
    "Parquet",
]


# --- restXml ser/de ---
def to_xml_text(value: InventoryFormat) -> str:
    return value


def from_xml_text(text: str) -> InventoryFormat:
    return cast(InventoryFormat, text)


def serialize_xml(value: InventoryFormat, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryFormat:
    return from_xml_text(el.text or "")
