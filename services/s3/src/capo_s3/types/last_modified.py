"""Generated from Smithy shape ``com.amazonaws.s3#LastModified``."""

import datetime
from typing import TypeAlias

from capo_s3._protocol.xml import Element, SubElement

LastModified: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: LastModified) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> LastModified:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: LastModified, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> LastModified:
    return from_xml_text(el.text or "")
