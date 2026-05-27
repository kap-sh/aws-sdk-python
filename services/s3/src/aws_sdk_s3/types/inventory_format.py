"""Generated from Smithy shape ``com.amazonaws.s3#InventoryFormat``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

InventoryFormat: TypeAlias = Literal[
    "CSV",
    "ORC",
    "Parquet",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "ORC",
        "Parquet",
    )
)


def to_xml_text(value: InventoryFormat) -> str:
    return value


def from_xml_text(text: str) -> InventoryFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InventoryFormat value: {text!r}")
    return cast(InventoryFormat, text)


def serialize_xml(value: InventoryFormat, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryFormat:
    return from_xml_text(el.text or "")
