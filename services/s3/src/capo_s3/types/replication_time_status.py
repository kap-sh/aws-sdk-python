"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationTimeStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ReplicationTimeStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: ReplicationTimeStatus) -> str:
    return value


def from_xml_text(text: str) -> ReplicationTimeStatus:
    return cast(ReplicationTimeStatus, text)


def serialize_xml(value: ReplicationTimeStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReplicationTimeStatus:
    return from_xml_text(el.text or "")
