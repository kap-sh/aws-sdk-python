"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockMode``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3ObjectLockMode: TypeAlias = Literal[
    "COMPLIANCE",
    "GOVERNANCE",
]


# --- restXml ser/de ---
def to_xml_text(value: S3ObjectLockMode) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockMode:
    return cast(S3ObjectLockMode, text)


def serialize_xml(value: S3ObjectLockMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockMode:
    return from_xml_text(el.text or "")
