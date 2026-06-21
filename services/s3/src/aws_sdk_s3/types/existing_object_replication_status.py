"""Generated from Smithy shape ``com.amazonaws.s3#ExistingObjectReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

ExistingObjectReplicationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: ExistingObjectReplicationStatus) -> str:
    return value


def from_xml_text(text: str) -> ExistingObjectReplicationStatus:
    return cast(ExistingObjectReplicationStatus, text)


def serialize_xml(
    value: ExistingObjectReplicationStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ExistingObjectReplicationStatus:
    return from_xml_text(el.text or "")
