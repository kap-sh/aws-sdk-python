"""Generated from Smithy shape ``com.amazonaws.cloudfront#timestamp``."""

import datetime
from typing import TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

timestamp: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: timestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_xml_text(text: str) -> timestamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: timestamp, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> timestamp:
    return from_xml_text(el.text or "")
