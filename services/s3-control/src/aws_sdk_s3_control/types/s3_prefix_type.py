"""Generated from Smithy shape ``com.amazonaws.s3control#S3PrefixType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

S3PrefixType: TypeAlias = Literal["Object",]


# --- restXml ser/de ---
def to_xml_text(value: S3PrefixType) -> str:
    return value


def from_xml_text(text: str) -> S3PrefixType:
    return cast(S3PrefixType, text)


def serialize_xml(value: S3PrefixType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3PrefixType:
    return from_xml_text(el.text or "")
