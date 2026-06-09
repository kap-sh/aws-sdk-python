"""Generated from Smithy shape ``com.amazonaws.s3#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

Type: TypeAlias = Literal[
    "CanonicalUser",
    "AmazonCustomerByEmail",
    "Group",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CanonicalUser",
        "AmazonCustomerByEmail",
        "Group",
    )
)


def to_xml_text(value: Type) -> str:
    return value


def from_xml_text(text: str) -> Type:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Type value: {text!r}")
    return cast(Type, text)


def serialize_xml(value: Type, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Type:
    return from_xml_text(el.text or "")
