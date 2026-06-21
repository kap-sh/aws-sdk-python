"""Generated from Smithy shape ``com.amazonaws.s3#StorageClassAnalysisSchemaVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

StorageClassAnalysisSchemaVersion: TypeAlias = Literal["V_1",]


# --- restXml ser/de ---
def to_xml_text(value: StorageClassAnalysisSchemaVersion) -> str:
    return value


def from_xml_text(text: str) -> StorageClassAnalysisSchemaVersion:
    return cast(StorageClassAnalysisSchemaVersion, text)


def serialize_xml(
    value: StorageClassAnalysisSchemaVersion, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> StorageClassAnalysisSchemaVersion:
    return from_xml_text(el.text or "")
