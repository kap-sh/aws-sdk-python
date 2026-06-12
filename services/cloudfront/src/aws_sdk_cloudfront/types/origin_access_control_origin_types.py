"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlOriginTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

OriginAccessControlOriginTypes: TypeAlias = Literal[
    "s3",
    "mediastore",
    "mediapackagev2",
    "lambda",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "s3",
        "mediastore",
        "mediapackagev2",
        "lambda",
    )
)


def to_xml_text(value: OriginAccessControlOriginTypes) -> str:
    return value


def from_xml_text(text: str) -> OriginAccessControlOriginTypes:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OriginAccessControlOriginTypes value: {text!r}"
        )
    return cast(OriginAccessControlOriginTypes, text)


def serialize_xml(
    value: OriginAccessControlOriginTypes, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OriginAccessControlOriginTypes:
    return from_xml_text(el.text or "")
