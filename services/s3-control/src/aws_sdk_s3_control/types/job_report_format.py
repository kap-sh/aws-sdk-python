"""Generated from Smithy shape ``com.amazonaws.s3control#JobReportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

JobReportFormat: TypeAlias = Literal["Report_CSV_20180820",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("Report_CSV_20180820",))


def to_xml_text(value: JobReportFormat) -> str:
    return value


def from_xml_text(text: str) -> JobReportFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown JobReportFormat value: {text!r}")
    return cast(JobReportFormat, text)


def serialize_xml(value: JobReportFormat, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobReportFormat:
    return from_xml_text(el.text or "")
