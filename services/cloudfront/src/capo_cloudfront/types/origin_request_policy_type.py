"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

OriginRequestPolicyType: TypeAlias = Literal[
    "managed",
    "custom",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginRequestPolicyType) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyType:
    return cast(OriginRequestPolicyType, text)


def serialize_xml(value: OriginRequestPolicyType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyType:
    return from_xml_text(el.text or "")
