"""Generated from Smithy shape ``com.amazonaws.s3#ReplicaModificationsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

ReplicaModificationsStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_xml_text(value: ReplicaModificationsStatus) -> str:
    return value


def from_xml_text(text: str) -> ReplicaModificationsStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ReplicaModificationsStatus value: {text!r}"
        )
    return cast(ReplicaModificationsStatus, text)


def serialize_xml(value: ReplicaModificationsStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReplicaModificationsStatus:
    return from_xml_text(el.text or "")
