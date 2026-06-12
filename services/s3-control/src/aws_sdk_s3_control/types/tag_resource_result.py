"""Generated from Smithy shape ``com.amazonaws.s3control#TagResourceResult``."""

from typing import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class TagResourceResult(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: TagResourceResult, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> TagResourceResult:
    out: TagResourceResult = {}  # type: ignore[typeddict-item]
    return out
