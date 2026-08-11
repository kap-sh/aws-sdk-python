"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime

from capo_route_53._protocol.xml import Element, SubElement


# --- restXml ser/de ---
def to_xml_text(value: datetime.datetime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_xml_text(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_xml(value: datetime.datetime, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> datetime.datetime:
    return from_xml_text(el.text or "")
