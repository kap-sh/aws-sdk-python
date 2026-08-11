"""Generated from Smithy shape ``com.amazonaws.s3#IfUnmodifiedSince``."""

import datetime
from typing import TypeAlias

from capo_s3._protocol.xml import Element, SubElement

IfUnmodifiedSince: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: IfUnmodifiedSince) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_xml_text(text: str) -> IfUnmodifiedSince:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: IfUnmodifiedSince, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> IfUnmodifiedSince:
    return from_xml_text(el.text or "")
