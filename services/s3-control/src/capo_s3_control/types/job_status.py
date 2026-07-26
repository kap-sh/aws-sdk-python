"""Generated from Smithy shape ``com.amazonaws.s3control#JobStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

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
def to_xml_text(value: JobStatus) -> str:
    return value


def from_xml_text(text: str) -> JobStatus:
    return cast(JobStatus, text)


def serialize_xml(value: JobStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobStatus:
    return from_xml_text(el.text or "")
