"""Generated from Smithy shape ``com.amazonaws.cloudfront#ValidationTokenHost``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ValidationTokenHost: TypeAlias = Literal[
    "cloudfront",
    "self-hosted",
]


# --- restXml ser/de ---
def to_xml_text(value: ValidationTokenHost) -> str:
    return value


def from_xml_text(text: str) -> ValidationTokenHost:
    return cast(ValidationTokenHost, text)


def serialize_xml(value: ValidationTokenHost, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ValidationTokenHost:
    return from_xml_text(el.text or "")
