"""Generated from Smithy shape ``com.amazonaws.s3#S3TablesBucketType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

S3TablesBucketType: TypeAlias = Literal[
    "aws",
    "customer",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aws",
        "customer",
    )
)


def to_xml_text(value: S3TablesBucketType) -> str:
    return value


def from_xml_text(text: str) -> S3TablesBucketType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3TablesBucketType value: {text!r}")
    return cast(S3TablesBucketType, text)


def serialize_xml(value: S3TablesBucketType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3TablesBucketType:
    return from_xml_text(el.text or "")
