"""Generated from Smithy shape ``com.amazonaws.s3#Payer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

Payer: TypeAlias = Literal[
    "Requester",
    "BucketOwner",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Requester",
        "BucketOwner",
    )
)


def to_xml_text(value: Payer) -> str:
    return value


def from_xml_text(text: str) -> Payer:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Payer value: {text!r}")
    return cast(Payer, text)


def serialize_xml(value: Payer, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Payer:
    return from_xml_text(el.text or "")
