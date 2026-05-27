"""Generated from Smithy shape ``com.amazonaws.s3#InventoryFrequency``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

InventoryFrequency: TypeAlias = Literal[
    "Daily",
    "Weekly",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Daily",
        "Weekly",
    )
)


def to_xml_text(value: InventoryFrequency) -> str:
    return value


def from_xml_text(text: str) -> InventoryFrequency:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InventoryFrequency value: {text!r}")
    return cast(InventoryFrequency, text)


def serialize_xml(value: InventoryFrequency, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryFrequency:
    return from_xml_text(el.text or "")
