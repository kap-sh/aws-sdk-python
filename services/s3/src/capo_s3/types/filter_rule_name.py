"""Generated from Smithy shape ``com.amazonaws.s3#FilterRuleName``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

FilterRuleName: TypeAlias = Literal[
    "prefix",
    "suffix",
]


# --- restXml ser/de ---
def to_xml_text(value: FilterRuleName) -> str:
    return value


def from_xml_text(text: str) -> FilterRuleName:
    return cast(FilterRuleName, text)


def serialize_xml(value: FilterRuleName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FilterRuleName:
    return from_xml_text(el.text or "")
