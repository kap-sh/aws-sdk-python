"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

FunctionStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- restXml ser/de ---
def to_xml_text(value: FunctionStage) -> str:
    return value


def from_xml_text(text: str) -> FunctionStage:
    return cast(FunctionStage, text)


def serialize_xml(value: FunctionStage, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FunctionStage:
    return from_xml_text(el.text or "")
