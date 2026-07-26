"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestFormat``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

JobManifestFormat: TypeAlias = Literal[
    "S3BatchOperations_CSV_20180820",
    "S3InventoryReport_CSV_20161130",
]


# --- restXml ser/de ---
def to_xml_text(value: JobManifestFormat) -> str:
    return value


def from_xml_text(text: str) -> JobManifestFormat:
    return cast(JobManifestFormat, text)


def serialize_xml(value: JobManifestFormat, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobManifestFormat:
    return from_xml_text(el.text or "")
