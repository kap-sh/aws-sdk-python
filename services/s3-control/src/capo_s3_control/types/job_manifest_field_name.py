"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestFieldName``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

JobManifestFieldName: TypeAlias = Literal[
    "Ignore",
    "Bucket",
    "Key",
    "VersionId",
]


# --- restXml ser/de ---
def to_xml_text(value: JobManifestFieldName) -> str:
    return value


def from_xml_text(text: str) -> JobManifestFieldName:
    return cast(JobManifestFieldName, text)


def serialize_xml(value: JobManifestFieldName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobManifestFieldName:
    return from_xml_text(el.text or "")
