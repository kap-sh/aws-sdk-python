"""Generated from Smithy shape ``com.amazonaws.s3#S3TablesBucketType``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

S3TablesBucketType: TypeAlias = Literal[
    "aws",
    "customer",
]


# --- restXml ser/de ---
def to_xml_text(value: S3TablesBucketType) -> str:
    return value


def from_xml_text(text: str) -> S3TablesBucketType:
    return cast(S3TablesBucketType, text)


def serialize_xml(value: S3TablesBucketType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3TablesBucketType:
    return from_xml_text(el.text or "")
