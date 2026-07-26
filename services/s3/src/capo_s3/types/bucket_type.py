"""Generated from Smithy shape ``com.amazonaws.s3#BucketType``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

BucketType: TypeAlias = Literal["Directory",]


# --- restXml ser/de ---
def to_xml_text(value: BucketType) -> str:
    return value


def from_xml_text(text: str) -> BucketType:
    return cast(BucketType, text)


def serialize_xml(value: BucketType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketType:
    return from_xml_text(el.text or "")
