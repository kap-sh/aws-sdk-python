"""Generated from Smithy shape ``com.amazonaws.s3#ObjectVersionStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ObjectVersionStorageClass: TypeAlias = Literal["STANDARD",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("STANDARD",))


def to_xml_text(value: ObjectVersionStorageClass) -> str:
    return value


def from_xml_text(text: str) -> ObjectVersionStorageClass:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ObjectVersionStorageClass value: {text!r}")
    return cast(ObjectVersionStorageClass, text)


def serialize_xml(value: ObjectVersionStorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectVersionStorageClass:
    return from_xml_text(el.text or "")
