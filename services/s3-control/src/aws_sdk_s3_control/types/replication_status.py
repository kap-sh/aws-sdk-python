"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

ReplicationStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "REPLICA",
    "NONE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "FAILED",
        "REPLICA",
        "NONE",
    )
)


def to_xml_text(value: ReplicationStatus) -> str:
    return value


def from_xml_text(text: str) -> ReplicationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReplicationStatus value: {text!r}")
    return cast(ReplicationStatus, text)


def serialize_xml(value: ReplicationStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReplicationStatus:
    return from_xml_text(el.text or "")
