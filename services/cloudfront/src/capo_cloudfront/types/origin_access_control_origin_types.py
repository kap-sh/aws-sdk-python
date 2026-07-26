"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlOriginTypes``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

OriginAccessControlOriginTypes: TypeAlias = Literal[
    "s3",
    "mediastore",
    "mediapackagev2",
    "lambda",
]


# --- restXml ser/de ---
def to_xml_text(value: OriginAccessControlOriginTypes) -> str:
    return value


def from_xml_text(text: str) -> OriginAccessControlOriginTypes:
    return cast(OriginAccessControlOriginTypes, text)


def serialize_xml(
    value: OriginAccessControlOriginTypes, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginAccessControlOriginTypes:
    return from_xml_text(el.text or "")
