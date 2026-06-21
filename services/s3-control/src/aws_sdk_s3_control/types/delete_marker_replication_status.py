"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteMarkerReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

DeleteMarkerReplicationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: DeleteMarkerReplicationStatus) -> str:
    return value


def from_xml_text(text: str) -> DeleteMarkerReplicationStatus:
    return cast(DeleteMarkerReplicationStatus, text)


def serialize_xml(
    value: DeleteMarkerReplicationStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DeleteMarkerReplicationStatus:
    return from_xml_text(el.text or "")
