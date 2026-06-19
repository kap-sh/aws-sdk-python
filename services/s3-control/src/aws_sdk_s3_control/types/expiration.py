"""Generated from Smithy shape ``com.amazonaws.s3control#Expiration``."""

import datetime
from typing import TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

Expiration: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: Expiration) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> Expiration:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: Expiration, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Expiration:
    return from_xml_text(el.text or "")
