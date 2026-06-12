"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

JobManifestFormat: TypeAlias = Literal[
    "S3BatchOperations_CSV_20180820",
    "S3InventoryReport_CSV_20161130",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3BatchOperations_CSV_20180820",
        "S3InventoryReport_CSV_20161130",
    )
)


def to_xml_text(value: JobManifestFormat) -> str:
    return value


def from_xml_text(text: str) -> JobManifestFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown JobManifestFormat value: {text!r}")
    return cast(JobManifestFormat, text)


def serialize_xml(value: JobManifestFormat, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobManifestFormat:
    return from_xml_text(el.text or "")
