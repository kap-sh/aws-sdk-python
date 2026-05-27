"""Generated from Smithy shape ``com.amazonaws.s3#RenameObjectOutput``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement


class RenameObjectOutput(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: RenameObjectOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> RenameObjectOutput:
    out: RenameObjectOutput = {}  # type: ignore[typeddict-item]
    return out
