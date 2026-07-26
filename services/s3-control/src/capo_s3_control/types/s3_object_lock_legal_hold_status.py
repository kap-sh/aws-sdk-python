"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockLegalHoldStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3ObjectLockLegalHoldStatus: TypeAlias = Literal[
    "OFF",
    "ON",
]


# --- restXml ser/de ---
def to_xml_text(value: S3ObjectLockLegalHoldStatus) -> str:
    return value


def from_xml_text(text: str) -> S3ObjectLockLegalHoldStatus:
    return cast(S3ObjectLockLegalHoldStatus, text)


def serialize_xml(
    value: S3ObjectLockLegalHoldStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ObjectLockLegalHoldStatus:
    return from_xml_text(el.text or "")
