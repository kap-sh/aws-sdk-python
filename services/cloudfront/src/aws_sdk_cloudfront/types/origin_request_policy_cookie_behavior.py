"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyCookieBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginRequestPolicyCookieBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "all",
    "allExcept",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "whitelist",
        "all",
        "allExcept",
    )
)


def to_xml_text(value: OriginRequestPolicyCookieBehavior) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyCookieBehavior:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OriginRequestPolicyCookieBehavior value: {text!r}"
        )
    return cast(OriginRequestPolicyCookieBehavior, text)


def serialize_xml(
    value: OriginRequestPolicyCookieBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyCookieBehavior:
    return from_xml_text(el.text or "")
