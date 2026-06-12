"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

FunctionStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPMENT",
        "LIVE",
    )
)


def to_xml_text(value: FunctionStage) -> str:
    return value


def from_xml_text(text: str) -> FunctionStage:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FunctionStage value: {text!r}")
    return cast(FunctionStage, text)


def serialize_xml(value: FunctionStage, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FunctionStage:
    return from_xml_text(el.text or "")
