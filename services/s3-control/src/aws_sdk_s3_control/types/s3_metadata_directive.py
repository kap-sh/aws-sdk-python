"""Generated from Smithy shape ``com.amazonaws.s3control#S3MetadataDirective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3MetadataDirective: TypeAlias = Literal[
    "COPY",
    "REPLACE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COPY",
        "REPLACE",
    )
)


def to_xml_text(value: S3MetadataDirective) -> str:
    return value


def from_xml_text(text: str) -> S3MetadataDirective:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3MetadataDirective value: {text!r}")
    return cast(S3MetadataDirective, text)


def serialize_xml(value: S3MetadataDirective, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3MetadataDirective:
    return from_xml_text(el.text or "")
