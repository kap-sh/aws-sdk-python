"""Generated from Smithy shape ``com.amazonaws.s3#RestoreExpiryDate``."""

import datetime
from typing import TypeAlias

from aws_sdk_s3._protocol.xml import Element, SubElement

RestoreExpiryDate: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: RestoreExpiryDate) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> RestoreExpiryDate:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: RestoreExpiryDate, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RestoreExpiryDate:
    return from_xml_text(el.text or "")
