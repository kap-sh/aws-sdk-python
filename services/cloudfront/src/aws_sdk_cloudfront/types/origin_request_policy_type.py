"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginRequestPolicyType: TypeAlias = Literal[
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


def to_xml_text(value: OriginRequestPolicyType) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OriginRequestPolicyType value: {text!r}")
    return cast(OriginRequestPolicyType, text)


def serialize_xml(value: OriginRequestPolicyType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyType:
    return from_xml_text(el.text or "")
