"""Generated from Smithy shape ``com.amazonaws.s3#InventoryIncludedObjectVersions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

InventoryIncludedObjectVersions: TypeAlias = Literal[
    "All",
    "Current",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Current",
    )
)


def to_xml_text(value: InventoryIncludedObjectVersions) -> str:
    return value


def from_xml_text(text: str) -> InventoryIncludedObjectVersions:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InventoryIncludedObjectVersions value: {text!r}"
        )
    return cast(InventoryIncludedObjectVersions, text)


def serialize_xml(
    value: InventoryIncludedObjectVersions, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryIncludedObjectVersions:
    return from_xml_text(el.text or "")
