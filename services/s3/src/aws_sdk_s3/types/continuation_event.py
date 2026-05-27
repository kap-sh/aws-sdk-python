"""Generated from Smithy shape ``com.amazonaws.s3#ContinuationEvent``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement


class ContinuationEvent(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: ContinuationEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ContinuationEvent:
    out: ContinuationEvent = {}  # type: ignore[typeddict-item]
    return out
