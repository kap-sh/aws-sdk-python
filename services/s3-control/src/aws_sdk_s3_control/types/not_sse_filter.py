"""Generated from Smithy shape ``com.amazonaws.s3control#NotSSEFilter``."""

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class NotSSEFilter(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NotSSEFilter, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NotSSEFilter:
    out: NotSSEFilter = {}  # type: ignore[typeddict-item]
    return out
