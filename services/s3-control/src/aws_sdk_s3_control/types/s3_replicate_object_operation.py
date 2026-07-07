"""Generated from Smithy shape ``com.amazonaws.s3control#S3ReplicateObjectOperation``."""

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class S3ReplicateObjectOperation(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: S3ReplicateObjectOperation, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> S3ReplicateObjectOperation:
    out: S3ReplicateObjectOperation = {}  # type: ignore[typeddict-item]
    return out
