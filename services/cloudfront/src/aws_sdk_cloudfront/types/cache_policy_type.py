"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

CachePolicyType: TypeAlias = Literal[
    "managed",
    "custom",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "managed",
        "custom",
    )
)


def to_xml_text(value: CachePolicyType) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CachePolicyType value: {text!r}")
    return cast(CachePolicyType, text)


def serialize_xml(value: CachePolicyType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyType:
    return from_xml_text(el.text or "")
