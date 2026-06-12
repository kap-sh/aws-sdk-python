"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlAllowMethodsValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

ResponseHeadersPolicyAccessControlAllowMethodsValues: TypeAlias = Literal[
    "GET",
    "POST",
    "OPTIONS",
    "PUT",
    "DELETE",
    "PATCH",
    "HEAD",
    "ALL",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "POST",
        "OPTIONS",
        "PUT",
        "DELETE",
        "PATCH",
        "HEAD",
        "ALL",
    )
)


def to_xml_text(value: ResponseHeadersPolicyAccessControlAllowMethodsValues) -> str:
    return value


def from_xml_text(text: str) -> ResponseHeadersPolicyAccessControlAllowMethodsValues:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ResponseHeadersPolicyAccessControlAllowMethodsValues value: {text!r}"
        )
    return cast(ResponseHeadersPolicyAccessControlAllowMethodsValues, text)


def serialize_xml(
    value: ResponseHeadersPolicyAccessControlAllowMethodsValues,
    parent: Element,
    tag: str,
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(
    el: Element,
) -> ResponseHeadersPolicyAccessControlAllowMethodsValues:
    return from_xml_text(el.text or "")
