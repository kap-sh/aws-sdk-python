"""Generated from Smithy shape ``com.amazonaws.s3control#OperationName``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

OperationName: TypeAlias = Literal[
    "LambdaInvoke",
    "S3PutObjectCopy",
    "S3PutObjectAcl",
    "S3PutObjectTagging",
    "S3DeleteObjectTagging",
    "S3InitiateRestoreObject",
    "S3PutObjectLegalHold",
    "S3PutObjectRetention",
    "S3ReplicateObject",
    "S3ComputeObjectChecksum",
    "S3UpdateObjectEncryption",
]


# --- restXml ser/de ---
def to_xml_text(value: OperationName) -> str:
    return value


def from_xml_text(text: str) -> OperationName:
    return cast(OperationName, text)


def serialize_xml(value: OperationName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OperationName:
    return from_xml_text(el.text or "")
