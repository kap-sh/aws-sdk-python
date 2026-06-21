"""Generated from Smithy shape ``com.amazonaws.s3control#S3GranteeTypeIdentifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

S3GranteeTypeIdentifier: TypeAlias = Literal[
    "id",
    "emailAddress",
    "uri",
]


# --- restXml ser/de ---
def to_xml_text(value: S3GranteeTypeIdentifier) -> str:
    return value


def from_xml_text(text: str) -> S3GranteeTypeIdentifier:
    return cast(S3GranteeTypeIdentifier, text)


def serialize_xml(value: S3GranteeTypeIdentifier, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3GranteeTypeIdentifier:
    return from_xml_text(el.text or "")
