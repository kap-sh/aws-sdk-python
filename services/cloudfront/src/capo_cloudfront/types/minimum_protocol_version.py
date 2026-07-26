"""Generated from Smithy shape ``com.amazonaws.cloudfront#MinimumProtocolVersion``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

MinimumProtocolVersion: TypeAlias = Literal[
    "SSLv3",
    "TLSv1",
    "TLSv1_2016",
    "TLSv1.1_2016",
    "TLSv1.2_2018",
    "TLSv1.2_2019",
    "TLSv1.2_2021",
    "TLSv1.3_2025",
    "TLSv1.2_2025",
]


# --- restXml ser/de ---
def to_xml_text(value: MinimumProtocolVersion) -> str:
    return value


def from_xml_text(text: str) -> MinimumProtocolVersion:
    return cast(MinimumProtocolVersion, text)


def serialize_xml(value: MinimumProtocolVersion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MinimumProtocolVersion:
    return from_xml_text(el.text or "")
