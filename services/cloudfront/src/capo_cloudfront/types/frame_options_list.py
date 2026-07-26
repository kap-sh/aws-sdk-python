"""Generated from Smithy shape ``com.amazonaws.cloudfront#FrameOptionsList``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

FrameOptionsList: TypeAlias = Literal[
    "DENY",
    "SAMEORIGIN",
]


# --- restXml ser/de ---
def to_xml_text(value: FrameOptionsList) -> str:
    return value


def from_xml_text(text: str) -> FrameOptionsList:
    return cast(FrameOptionsList, text)


def serialize_xml(value: FrameOptionsList, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FrameOptionsList:
    return from_xml_text(el.text or "")
