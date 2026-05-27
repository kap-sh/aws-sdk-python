"""Generated from Smithy shape ``com.amazonaws.s3#SimplePrefix``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement


class SimplePrefix(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: SimplePrefix, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> SimplePrefix:
    out: SimplePrefix = {}  # type: ignore[typeddict-item]
    return out
