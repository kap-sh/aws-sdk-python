"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyQueryStringBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

CachePolicyQueryStringBehavior: TypeAlias = Literal[
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


def to_xml_text(value: CachePolicyQueryStringBehavior) -> str:
    return value


def from_xml_text(text: str) -> CachePolicyQueryStringBehavior:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CachePolicyQueryStringBehavior value: {text!r}"
        )
    return cast(CachePolicyQueryStringBehavior, text)


def serialize_xml(
    value: CachePolicyQueryStringBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CachePolicyQueryStringBehavior:
    return from_xml_text(el.text or "")
