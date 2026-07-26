"""Generated from Smithy shape ``com.amazonaws.s3control#JobReportScope``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

JobReportScope: TypeAlias = Literal[
    "AllTasks",
    "FailedTasksOnly",
]


# --- restXml ser/de ---
def to_xml_text(value: JobReportScope) -> str:
    return value


def from_xml_text(text: str) -> JobReportScope:
    return cast(JobReportScope, text)


def serialize_xml(value: JobReportScope, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobReportScope:
    return from_xml_text(el.text or "")
