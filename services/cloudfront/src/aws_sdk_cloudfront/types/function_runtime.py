"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionRuntime``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

FunctionRuntime: TypeAlias = Literal[
    "cloudfront-js-1.0",
    "cloudfront-js-2.0",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cloudfront-js-1.0",
        "cloudfront-js-2.0",
    )
)


def to_xml_text(value: FunctionRuntime) -> str:
    return value


def from_xml_text(text: str) -> FunctionRuntime:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FunctionRuntime value: {text!r}")
    return cast(FunctionRuntime, text)


def serialize_xml(value: FunctionRuntime, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FunctionRuntime:
    return from_xml_text(el.text or "")
