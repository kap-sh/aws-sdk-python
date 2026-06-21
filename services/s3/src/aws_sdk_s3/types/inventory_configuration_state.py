"""Generated from Smithy shape ``com.amazonaws.s3#InventoryConfigurationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

InventoryConfigurationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restXml ser/de ---
def to_xml_text(value: InventoryConfigurationState) -> str:
    return value


def from_xml_text(text: str) -> InventoryConfigurationState:
    return cast(InventoryConfigurationState, text)


def serialize_xml(
    value: InventoryConfigurationState, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryConfigurationState:
    return from_xml_text(el.text or "")
