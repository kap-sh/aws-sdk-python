"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionBlob``."""

import base64
from typing import TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

FunctionBlob: TypeAlias = bytes


# --- restXml ser/de ---
def to_xml_text(value: FunctionBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def from_xml_text(text: str) -> FunctionBlob:
    return base64.b64decode(text)


def serialize_xml(value: FunctionBlob, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FunctionBlob:
    return from_xml_text(el.text or "")
