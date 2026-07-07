"""Generated from Smithy shape ``com.amazonaws.s3control#SSES3Encryption``."""

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class SSES3Encryption(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: SSES3Encryption, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> SSES3Encryption:
    out: SSES3Encryption = {}  # type: ignore[typeddict-item]
    return out
