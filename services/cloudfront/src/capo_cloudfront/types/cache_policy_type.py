"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

CachePolicyType: TypeAlias = Literal[
    "managed",
    "custom",
]


# --- restXml ser/de ---
def to_xml_text(value: CachePolicyType) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyType:
    return cast(CachePolicyType, text)


def serialize_xml(value: CachePolicyType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyType:
    return from_xml_text(el.text or "")
