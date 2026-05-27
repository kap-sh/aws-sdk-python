"""Generated from Smithy shape ``com.amazonaws.s3#EndEvent``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement


class EndEvent(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: EndEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EndEvent:
    out: EndEvent = {}  # type: ignore[typeddict-item]
    return out
