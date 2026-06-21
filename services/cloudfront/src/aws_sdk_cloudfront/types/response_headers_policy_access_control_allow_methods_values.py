"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlAllowMethodsValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

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
def to_xml_text(value: ResponseHeadersPolicyAccessControlAllowMethodsValues) -> str:
    return value


def from_xml_text(text: str) -> ResponseHeadersPolicyAccessControlAllowMethodsValues:
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
