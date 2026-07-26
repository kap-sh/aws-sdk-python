"""Generated from Smithy shape ``com.amazonaws.s3control#TagResourceResult``."""

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement


class TagResourceResult(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: TagResourceResult, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> TagResourceResult:
    out: TagResourceResult = {}  # type: ignore[typeddict-item]
    return out
