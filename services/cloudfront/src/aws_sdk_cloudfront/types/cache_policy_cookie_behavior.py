"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyCookieBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

CachePolicyCookieBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "allExcept",
    "all",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "whitelist",
        "allExcept",
        "all",
    )
)


def to_xml_text(value: CachePolicyCookieBehavior) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyCookieBehavior:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CachePolicyCookieBehavior value: {text!r}")
    return cast(CachePolicyCookieBehavior, text)


def serialize_xml(value: CachePolicyCookieBehavior, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyCookieBehavior:
    return from_xml_text(el.text or "")
