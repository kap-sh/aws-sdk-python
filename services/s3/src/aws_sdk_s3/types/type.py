"""Generated from Smithy shape ``com.amazonaws.s3#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

Type: TypeAlias = Literal[
    "CanonicalUser",
    "AmazonCustomerByEmail",
    "Group",
]


# --- restXml ser/de ---
def to_xml_text(value: Type) -> str:
    return value


def from_xml_text(text: str) -> Type:
    return cast(Type, text)


def serialize_xml(value: Type, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Type:
    return from_xml_text(el.text or "")
