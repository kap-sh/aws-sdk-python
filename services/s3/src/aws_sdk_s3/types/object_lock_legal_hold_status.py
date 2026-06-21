"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockLegalHoldStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

ObjectLockLegalHoldStatus: TypeAlias = Literal[
    "ON",
    "OFF",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLockLegalHoldStatus) -> str:
    return value


def from_xml_text(text: str) -> ObjectLockLegalHoldStatus:
    return cast(ObjectLockLegalHoldStatus, text)


def serialize_xml(value: ObjectLockLegalHoldStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLockLegalHoldStatus:
    return from_xml_text(el.text or "")
