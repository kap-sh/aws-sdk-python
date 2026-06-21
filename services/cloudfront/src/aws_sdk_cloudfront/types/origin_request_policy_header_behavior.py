"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyHeaderBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

OriginRequestPolicyHeaderBehavior: TypeAlias = Literal[
    "none",
    "whitelist",
    "allViewer",
    "allViewerAndWhitelistCloudFront",
    "allExcept",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginRequestPolicyHeaderBehavior) -> str:
    return value


def from_xml_text(text: str) -> OriginRequestPolicyHeaderBehavior:
    return cast(OriginRequestPolicyHeaderBehavior, text)


def serialize_xml(
    value: OriginRequestPolicyHeaderBehavior, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginRequestPolicyHeaderBehavior:
    return from_xml_text(el.text or "")
