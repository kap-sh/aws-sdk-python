"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionEventObject``."""

import base64
from typing import TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

FunctionEventObject: TypeAlias = bytes


# --- restXml ser/de ---
def to_xml_text(value: FunctionEventObject) -> str:
    return base64.b64encode(value).decode("ascii")


def from_xml_text(text: str) -> FunctionEventObject:
    return base64.b64decode(text)


def serialize_xml(value: FunctionEventObject, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FunctionEventObject:
    return from_xml_text(el.text or "")
