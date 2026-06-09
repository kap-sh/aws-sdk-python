"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockEnabled``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ObjectLockEnabled: TypeAlias = Literal["Enabled",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("Enabled",))


def to_xml_text(value: ObjectLockEnabled) -> str:
    return value


def from_xml_text(text: str) -> ObjectLockEnabled:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ObjectLockEnabled value: {text!r}")
    return cast(ObjectLockEnabled, text)


def serialize_xml(value: ObjectLockEnabled, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLockEnabled:
    return from_xml_text(el.text or "")
