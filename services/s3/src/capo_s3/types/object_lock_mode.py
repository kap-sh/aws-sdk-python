"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockMode``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ObjectLockMode: TypeAlias = Literal[
    "GOVERNANCE",
    "COMPLIANCE",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLockMode) -> str:
    return value


def from_xml_text(text: str) -> ObjectLockMode:
    return cast(ObjectLockMode, text)


def serialize_xml(value: ObjectLockMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLockMode:
    return from_xml_text(el.text or "")
