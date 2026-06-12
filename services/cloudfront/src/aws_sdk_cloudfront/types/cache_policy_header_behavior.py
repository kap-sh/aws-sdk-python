"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyHeaderBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

CachePolicyHeaderBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "whitelist",
    )
)


def to_xml_text(value: CachePolicyHeaderBehavior) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyHeaderBehavior:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CachePolicyHeaderBehavior value: {text!r}")
    return cast(CachePolicyHeaderBehavior, text)


def serialize_xml(value: CachePolicyHeaderBehavior, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyHeaderBehavior:
    return from_xml_text(el.text or "")
