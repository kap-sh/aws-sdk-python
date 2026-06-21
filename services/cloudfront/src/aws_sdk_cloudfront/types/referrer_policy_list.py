"""Generated from Smithy shape ``com.amazonaws.cloudfront#ReferrerPolicyList``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

ReferrerPolicyList: TypeAlias = Literal[
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]


# --- restXml ser/de ---
def to_xml_text(value: ReferrerPolicyList) -> str:
    return value


def from_xml_text(text: str) -> ReferrerPolicyList:
    return cast(ReferrerPolicyList, text)


def serialize_xml(value: ReferrerPolicyList, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReferrerPolicyList:
    return from_xml_text(el.text or "")
