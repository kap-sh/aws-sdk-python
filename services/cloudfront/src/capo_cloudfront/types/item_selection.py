"""Generated from Smithy shape ``com.amazonaws.cloudfront#ItemSelection``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ItemSelection: TypeAlias = Literal[
    "none",
    "whitelist",
    "all",
]


# --- restXml ser/de ---
def to_xml_text(value: ItemSelection) -> str:
    return value


def from_xml_text(text: str) -> ItemSelection:
    return cast(ItemSelection, text)


def serialize_xml(value: ItemSelection, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ItemSelection:
    return from_xml_text(el.text or "")
