"""Generated from Smithy shape ``com.amazonaws.s3control#S3Permission``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3Permission: TypeAlias = Literal[
    "FULL_CONTROL",
    "READ",
    "WRITE",
    "READ_ACP",
    "WRITE_ACP",
]


# --- restXml ser/de ---
def to_xml_text(value: S3Permission) -> str:
    return value


def from_xml_text(text: str) -> S3Permission:
    return cast(S3Permission, text)


def serialize_xml(value: S3Permission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3Permission:
    return from_xml_text(el.text or "")
