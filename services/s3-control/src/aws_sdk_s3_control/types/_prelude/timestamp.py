"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime

from aws_sdk_s3_control._protocol.xml import Element, SubElement


# --- restXml ser/de ---
def to_xml_text(value: datetime.datetime) -> str:
    return value.isoformat()


def from_xml_text(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text)


def serialize_xml(value: datetime.datetime, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> datetime.datetime:
    return from_xml_text(el.text or "")
