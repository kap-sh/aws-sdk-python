"""Generated from Smithy shape ``com.amazonaws.cloudfront#ItemSelection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

ItemSelection: TypeAlias = Literal[
    "none",
    "whitelist",
    "all",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "whitelist",
        "all",
    )
)


def to_xml_text(value: ItemSelection) -> str:
    return value


def from_xml_text(text: str) -> ItemSelection:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ItemSelection value: {text!r}")
    return cast(ItemSelection, text)


def serialize_xml(value: ItemSelection, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ItemSelection:
    return from_xml_text(el.text or "")
