"""Generated from Smithy shape ``com.amazonaws.s3control#BucketCannedACL``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

BucketCannedACL: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
]


# --- restXml ser/de ---
def to_xml_text(value: BucketCannedACL) -> str:
    return value


def from_xml_text(text: str) -> BucketCannedACL:
    return cast(BucketCannedACL, text)


def serialize_xml(value: BucketCannedACL, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketCannedACL:
    return from_xml_text(el.text or "")
