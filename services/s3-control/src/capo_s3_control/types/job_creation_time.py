"""Generated from Smithy shape ``com.amazonaws.s3control#JobCreationTime``."""

import datetime
from typing import TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

JobCreationTime: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: JobCreationTime) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> JobCreationTime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: JobCreationTime, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobCreationTime:
    return from_xml_text(el.text or "")
