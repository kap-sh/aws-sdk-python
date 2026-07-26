"""Generated from Smithy shape ``com.amazonaws.cloudfront#ViewerProtocolPolicy``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ViewerProtocolPolicy: TypeAlias = Literal[
    "allow-all",
    "https-only",
    "redirect-to-https",
]


# --- restXml ser/de ---
def to_xml_text(value: ViewerProtocolPolicy) -> str:
    return value


def from_xml_text(text: str) -> ViewerProtocolPolicy:
    return cast(ViewerProtocolPolicy, text)


def serialize_xml(value: ViewerProtocolPolicy, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ViewerProtocolPolicy:
    return from_xml_text(el.text or "")
