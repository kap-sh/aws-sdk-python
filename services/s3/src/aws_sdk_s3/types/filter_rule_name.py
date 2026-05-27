"""Generated from Smithy shape ``com.amazonaws.s3#FilterRuleName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

FilterRuleName: TypeAlias = Literal[
    "prefix",
    "suffix",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "prefix",
        "suffix",
    )
)


def to_xml_text(value: FilterRuleName) -> str:
    return value


def from_xml_text(text: str) -> FilterRuleName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FilterRuleName value: {text!r}")
    return cast(FilterRuleName, text)


def serialize_xml(value: FilterRuleName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> FilterRuleName:
    return from_xml_text(el.text or "")
