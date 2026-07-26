"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockRetentionMode``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ObjectLockRetentionMode: TypeAlias = Literal[
    "GOVERNANCE",
    "COMPLIANCE",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLockRetentionMode) -> str:
    return value


def from_xml_text(text: str) -> ObjectLockRetentionMode:
    return cast(ObjectLockRetentionMode, text)


def serialize_xml(value: ObjectLockRetentionMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLockRetentionMode:
    return from_xml_text(el.text or "")
