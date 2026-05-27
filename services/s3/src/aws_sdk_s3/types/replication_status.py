"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

ReplicationStatus: TypeAlias = Literal[
    "COMPLETE",
    "PENDING",
    "FAILED",
    "REPLICA",
    "COMPLETED",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "PENDING",
        "FAILED",
        "REPLICA",
        "COMPLETED",
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
