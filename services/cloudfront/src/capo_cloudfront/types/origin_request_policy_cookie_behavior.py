"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyCookieBehavior``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

OriginRequestPolicyCookieBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "all",
    "allExcept",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginRequestPolicyCookieBehavior) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyCookieBehavior:
    return cast(OriginRequestPolicyCookieBehavior, text)


def serialize_xml(
    value: OriginRequestPolicyCookieBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyCookieBehavior:
    return from_xml_text(el.text or "")
