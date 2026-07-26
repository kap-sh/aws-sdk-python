"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyHeaderBehavior``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

CachePolicyHeaderBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
]


# --- restXml ser/de ---
def to_xml_text(value: CachePolicyHeaderBehavior) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyHeaderBehavior:
    return cast(CachePolicyHeaderBehavior, text)


def serialize_xml(value: CachePolicyHeaderBehavior, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyHeaderBehavior:
    return from_xml_text(el.text or "")
