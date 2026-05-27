"""Generated from Smithy shape ``com.amazonaws.s3#TaggingDirective``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

TaggingDirective: TypeAlias = Literal[
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


def to_xml_text(value: TaggingDirective) -> str:
    return value


def from_xml_text(text: str) -> TaggingDirective:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TaggingDirective value: {text!r}")
    return cast(TaggingDirective, text)


def serialize_xml(value: TaggingDirective, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TaggingDirective:
    return from_xml_text(el.text or "")
