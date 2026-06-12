"""Generated from Smithy shape ``com.amazonaws.s3control#SSECFilter``."""

from typing import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class SSECFilter(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: SSECFilter, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> SSECFilter:
    out: SSECFilter = {}  # type: ignore[typeddict-item]
    return out
