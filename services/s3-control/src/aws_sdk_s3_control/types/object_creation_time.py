"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectCreationTime``."""

import datetime
from typing import TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

ObjectCreationTime: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: ObjectCreationTime) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> ObjectCreationTime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: ObjectCreationTime, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectCreationTime:
    return from_xml_text(el.text or "")
