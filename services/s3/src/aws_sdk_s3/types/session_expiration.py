"""Generated from Smithy shape ``com.amazonaws.s3#SessionExpiration``."""

import datetime
from typing import TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

SessionExpiration: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: SessionExpiration) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> SessionExpiration:
    return datetime.datetime.fromisoformat(text)


def serialize_xml(value: SessionExpiration, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> SessionExpiration:
    return from_xml_text(el.text or "")
