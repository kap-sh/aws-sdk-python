"""Generated from Smithy shape ``com.amazonaws.s3control#BucketVersioningStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

BucketVersioningStatus: TypeAlias = Literal[
    "Enabled",
    "Suspended",
]


# --- restXml ser/de ---
def to_xml_text(value: BucketVersioningStatus) -> str:
    return value


def from_xml_text(text: str) -> BucketVersioningStatus:
    return cast(BucketVersioningStatus, text)


def serialize_xml(value: BucketVersioningStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketVersioningStatus:
    return from_xml_text(el.text or "")
