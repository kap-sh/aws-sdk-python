"""Generated from Smithy shape ``com.amazonaws.s3#Body``."""

from typing import TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement
import base64

Body: TypeAlias = bytes


# --- restXml ser/de ---
def to_xml_text(value: Body) -> str:
    return base64.b64encode(value).decode("ascii")


def from_xml_text(text: str) -> Body:
    return base64.b64decode(text)


def serialize_xml(value: Body, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Body:
    return from_xml_text(el.text or "")
