"""Generated from Smithy shape ``com.amazonaws.s3control#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "Active",
    "Cancelled",
    "Cancelling",
    "Complete",
    "Completing",
    "Failed",
    "Failing",
    "New",
    "Paused",
    "Pausing",
    "Preparing",
    "Ready",
    "Suspended",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Cancelled",
        "Cancelling",
        "Complete",
        "Completing",
        "Failed",
        "Failing",
        "New",
        "Paused",
        "Pausing",
        "Preparing",
        "Ready",
        "Suspended",
    )
)


def to_xml_text(value: JobStatus) -> str:
    return value


def from_xml_text(text: str) -> JobStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {text!r}")
    return cast(JobStatus, text)


def serialize_xml(value: JobStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobStatus:
    return from_xml_text(el.text or "")
