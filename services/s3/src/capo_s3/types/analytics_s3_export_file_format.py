"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsS3ExportFileFormat``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

AnalyticsS3ExportFileFormat: TypeAlias = Literal["CSV",]


# --- restXml ser/de ---
def to_xml_text(value: AnalyticsS3ExportFileFormat) -> str:
    return value


def from_xml_text(text: str) -> AnalyticsS3ExportFileFormat:
    return cast(AnalyticsS3ExportFileFormat, text)


def serialize_xml(
    value: AnalyticsS3ExportFileFormat, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AnalyticsS3ExportFileFormat:
    return from_xml_text(el.text or "")
