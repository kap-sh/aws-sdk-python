"""Generated from Smithy shape ``com.amazonaws.s3control#UntagResourceResult``."""

from typing import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class UntagResourceResult(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: UntagResourceResult, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UntagResourceResult:
    out: UntagResourceResult = {}  # type: ignore[typeddict-item]
    return out
