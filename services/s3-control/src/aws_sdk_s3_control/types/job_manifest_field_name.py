"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestFieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

JobManifestFieldName: TypeAlias = Literal[
    "Ignore",
    "Bucket",
    "Key",
    "VersionId",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ignore",
        "Bucket",
        "Key",
        "VersionId",
    )
)


def to_xml_text(value: JobManifestFieldName) -> str:
    return value


def from_xml_text(text: str) -> JobManifestFieldName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown JobManifestFieldName value: {text!r}")
    return cast(JobManifestFieldName, text)


def serialize_xml(value: JobManifestFieldName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> JobManifestFieldName:
    return from_xml_text(el.text or "")
