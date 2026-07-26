"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyQueryStringBehavior``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

CachePolicyQueryStringBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "allExcept",
    "all",
]


# --- restXml ser/de ---
def to_xml_text(value: CachePolicyQueryStringBehavior) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyQueryStringBehavior:
    return cast(CachePolicyQueryStringBehavior, text)


def serialize_xml(
    value: CachePolicyQueryStringBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyQueryStringBehavior:
    return from_xml_text(el.text or "")
