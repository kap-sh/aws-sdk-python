"""Generated from Smithy shape ``com.amazonaws.s3control#Date``."""

import datetime
from typing import TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

Date: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: Date) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> Date:
    return datetime.datetime.fromisoformat(text)


def serialize_xml(value: Date, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Date:
    return from_xml_text(el.text or "")
