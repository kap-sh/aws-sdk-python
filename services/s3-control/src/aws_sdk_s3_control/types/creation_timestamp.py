"""Generated from Smithy shape ``com.amazonaws.s3control#CreationTimestamp``."""

import datetime
from typing import TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

CreationTimestamp: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: CreationTimestamp) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> CreationTimestamp:
    return datetime.datetime.fromisoformat(text)


def serialize_xml(value: CreationTimestamp, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CreationTimestamp:
    return from_xml_text(el.text or "")
