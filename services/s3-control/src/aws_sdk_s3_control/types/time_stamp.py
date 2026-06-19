"""Generated from Smithy shape ``com.amazonaws.s3control#TimeStamp``."""

import datetime
from typing import TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

TimeStamp: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: TimeStamp) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> TimeStamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: TimeStamp, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TimeStamp:
    return from_xml_text(el.text or "")
