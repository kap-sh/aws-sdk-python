"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicaModificationsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

ReplicaModificationsStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: ReplicaModificationsStatus) -> str:
    return value


def from_xml_text(text: str) -> ReplicaModificationsStatus:
    return cast(ReplicaModificationsStatus, text)


def serialize_xml(value: ReplicaModificationsStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReplicaModificationsStatus:
    return from_xml_text(el.text or "")
