"""Generated from Smithy shape ``com.amazonaws.s3#AbortDate``."""

import datetime
from typing import TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

AbortDate: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: AbortDate) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> AbortDate:
    return datetime.datetime.fromisoformat(text)


def serialize_xml(value: AbortDate, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AbortDate:
    return from_xml_text(el.text or "")
