"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyQueryStringBehavior``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

OriginRequestPolicyQueryStringBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "all",
    "allExcept",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginRequestPolicyQueryStringBehavior) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyQueryStringBehavior:
    return cast(OriginRequestPolicyQueryStringBehavior, text)


def serialize_xml(
    value: OriginRequestPolicyQueryStringBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyQueryStringBehavior:
    return from_xml_text(el.text or "")
