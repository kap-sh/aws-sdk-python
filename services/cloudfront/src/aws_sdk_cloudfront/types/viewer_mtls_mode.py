"""Generated from Smithy shape ``com.amazonaws.cloudfront#ViewerMtlsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

ViewerMtlsMode: TypeAlias = Literal[
    "required",
    "optional",
    "passthrough",
]


# --- restXml ser/de ---
def to_xml_text(value: ViewerMtlsMode) -> str:
    return value


def from_xml_text(text: str) -> ViewerMtlsMode:
    return cast(ViewerMtlsMode, text)


def serialize_xml(value: ViewerMtlsMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ViewerMtlsMode:
    return from_xml_text(el.text or "")
