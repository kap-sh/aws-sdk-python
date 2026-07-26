"""Generated from Smithy shape ``com.amazonaws.s3control#SSES3``."""

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement


class SSES3(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: SSES3, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> SSES3:
    out: SSES3 = {}  # type: ignore[typeddict-item]
    return out
