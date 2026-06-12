"""Generated from Smithy shape ``com.amazonaws.s3control#GranteeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

GranteeType: TypeAlias = Literal[
    "DIRECTORY_USER",
    "DIRECTORY_GROUP",
    "IAM",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECTORY_USER",
        "DIRECTORY_GROUP",
        "IAM",
    )
)


def to_xml_text(value: GranteeType) -> str:
    return value


def from_xml_text(text: str) -> GranteeType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown GranteeType value: {text!r}")
    return cast(GranteeType, text)


def serialize_xml(value: GranteeType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> GranteeType:
    return from_xml_text(el.text or "")
