"""Generated from Smithy shape ``com.amazonaws.s3#JSONType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

JSONType: TypeAlias = Literal[
    "DOCUMENT",
    "LINES",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT",
        "LINES",
    )
)


def to_xml_text(value: JSONType) -> str:
    return value


def from_xml_text(text: str) -> JSONType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown JSONType value: {text!r}")
    return cast(JSONType, text)


def serialize_xml(value: JSONType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JSONType:
    return from_xml_text(el.text or "")
