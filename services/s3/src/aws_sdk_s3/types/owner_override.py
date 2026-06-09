"""Generated from Smithy shape ``com.amazonaws.s3#OwnerOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

OwnerOverride: TypeAlias = Literal["Destination",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("Destination",))


def to_xml_text(value: OwnerOverride) -> str:
    return value


def from_xml_text(text: str) -> OwnerOverride:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OwnerOverride value: {text!r}")
    return cast(OwnerOverride, text)


def serialize_xml(value: OwnerOverride, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OwnerOverride:
    return from_xml_text(el.text or "")
