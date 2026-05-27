"""Generated from Smithy shape ``com.amazonaws.s3#ServerSideEncryption``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

ServerSideEncryption: TypeAlias = Literal[
    "AES256",
    "aws:fsx",
    "aws:kms",
    "aws:kms:dsse",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES256",
        "aws:fsx",
        "aws:kms",
        "aws:kms:dsse",
    )
)


def to_xml_text(value: ServerSideEncryption) -> str:
    return value


def from_xml_text(text: str) -> ServerSideEncryption:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServerSideEncryption value: {text!r}")
    return cast(ServerSideEncryption, text)


def serialize_xml(value: ServerSideEncryption, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ServerSideEncryption:
    return from_xml_text(el.text or "")
