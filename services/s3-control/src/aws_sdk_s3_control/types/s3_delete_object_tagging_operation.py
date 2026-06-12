"""Generated from Smithy shape ``com.amazonaws.s3control#S3DeleteObjectTaggingOperation``."""

from typing import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class S3DeleteObjectTaggingOperation(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: S3DeleteObjectTaggingOperation, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> S3DeleteObjectTaggingOperation:
    out: S3DeleteObjectTaggingOperation = {}  # type: ignore[typeddict-item]
    return out
