"""Generated from Smithy shape ``com.amazonaws.s3control#SSES3Filter``."""

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class SSES3Filter(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: SSES3Filter, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> SSES3Filter:
    out: SSES3Filter = {}  # type: ignore[typeddict-item]
    return out
