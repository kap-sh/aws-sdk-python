"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyHeaderBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginRequestPolicyHeaderBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "allViewer",
    "allViewerAndWhitelistCloudFront",
    "allExcept",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "whitelist",
        "allViewer",
        "allViewerAndWhitelistCloudFront",
        "allExcept",
    )
)


def to_xml_text(value: OriginRequestPolicyHeaderBehavior) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyHeaderBehavior:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OriginRequestPolicyHeaderBehavior value: {text!r}"
        )
    return cast(OriginRequestPolicyHeaderBehavior, text)


def serialize_xml(
    value: OriginRequestPolicyHeaderBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyHeaderBehavior:
    return from_xml_text(el.text or "")
