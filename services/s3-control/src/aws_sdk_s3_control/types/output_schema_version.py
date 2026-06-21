"""Generated from Smithy shape ``com.amazonaws.s3control#OutputSchemaVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

OutputSchemaVersion: TypeAlias = Literal["V_1",]


# --- restXml ser/de ---
def to_xml_text(value: OutputSchemaVersion) -> str:
    return value


def from_xml_text(text: str) -> OutputSchemaVersion:
    return cast(OutputSchemaVersion, text)


def serialize_xml(value: OutputSchemaVersion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OutputSchemaVersion:
    return from_xml_text(el.text or "")
