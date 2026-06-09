"""Generated from Smithy shape ``com.amazonaws.s3#MetadataDirective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

MetadataDirective: TypeAlias = Literal[
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


def to_xml_text(value: MetadataDirective) -> str:
    return value


def from_xml_text(text: str) -> MetadataDirective:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MetadataDirective value: {text!r}")
    return cast(MetadataDirective, text)


def serialize_xml(value: MetadataDirective, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MetadataDirective:
    return from_xml_text(el.text or "")
