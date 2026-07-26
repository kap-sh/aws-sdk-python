"""Generated from Smithy shape ``com.amazonaws.s3#InventoryIncludedObjectVersions``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

InventoryIncludedObjectVersions: TypeAlias = Literal[
    "All",
    "Current",
]


# --- restXml ser/de ---
def to_xml_text(value: InventoryIncludedObjectVersions) -> str:
    return value


def from_xml_text(text: str) -> InventoryIncludedObjectVersions:
    return cast(InventoryIncludedObjectVersions, text)


def serialize_xml(
    value: InventoryIncludedObjectVersions, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryIncludedObjectVersions:
    return from_xml_text(el.text or "")
