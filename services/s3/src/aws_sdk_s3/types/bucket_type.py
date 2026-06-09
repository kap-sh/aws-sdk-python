"""Generated from Smithy shape ``com.amazonaws.s3#BucketType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

BucketType: TypeAlias = Literal["Directory",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("Directory",))


def to_xml_text(value: BucketType) -> str:
    return value


def from_xml_text(text: str) -> BucketType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketType value: {text!r}")
    return cast(BucketType, text)


def serialize_xml(value: BucketType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketType:
    return from_xml_text(el.text or "")
