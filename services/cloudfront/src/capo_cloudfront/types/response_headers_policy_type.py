"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ResponseHeadersPolicyType: TypeAlias = Literal[
    "managed",
    "custom",
]


# --- restXml ser/de ---
def to_xml_text(value: ResponseHeadersPolicyType) -> str:
    return value


def from_xml_text(text: str) -> ResponseHeadersPolicyType:
    return cast(ResponseHeadersPolicyType, text)


def serialize_xml(value: ResponseHeadersPolicyType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ResponseHeadersPolicyType:
    return from_xml_text(el.text or "")
