"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import base64

from capo_route_53._protocol.xml import Element, SubElement


# --- restXml ser/de ---
def to_xml_text(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def from_xml_text(text: str) -> bytes:
    return base64.b64decode(text)


def serialize_xml(value: bytes, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> bytes:
    return from_xml_text(el.text or "")
