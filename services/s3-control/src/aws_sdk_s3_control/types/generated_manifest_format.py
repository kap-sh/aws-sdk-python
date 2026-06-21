"""Generated from Smithy shape ``com.amazonaws.s3control#GeneratedManifestFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

GeneratedManifestFormat: TypeAlias = Literal["S3InventoryReport_CSV_20211130",]


# --- restXml ser/de ---
def to_xml_text(value: GeneratedManifestFormat) -> str:
    return value


def from_xml_text(text: str) -> GeneratedManifestFormat:
    return cast(GeneratedManifestFormat, text)


def serialize_xml(value: GeneratedManifestFormat, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> GeneratedManifestFormat:
    return from_xml_text(el.text or "")
