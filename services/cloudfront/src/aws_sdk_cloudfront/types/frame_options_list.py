"""Generated from Smithy shape ``com.amazonaws.cloudfront#FrameOptionsList``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

FrameOptionsList: TypeAlias = Literal[
    "DENY",
    "SAMEORIGIN",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DENY",
        "SAMEORIGIN",
    )
)


def to_xml_text(value: FrameOptionsList) -> str:
    return value


def from_xml_text(text: str) -> FrameOptionsList:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FrameOptionsList value: {text!r}")
    return cast(FrameOptionsList, text)


def serialize_xml(value: FrameOptionsList, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FrameOptionsList:
    return from_xml_text(el.text or "")
