"""Generated from Smithy shape ``com.amazonaws.s3control#SuspendedDate``."""

import datetime
from typing import TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

SuspendedDate: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: SuspendedDate) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> SuspendedDate:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: SuspendedDate, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SuspendedDate:
    return from_xml_text(el.text or "")
