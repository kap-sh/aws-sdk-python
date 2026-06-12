"""Generated from Smithy shape ``com.amazonaws.s3control#BucketLocationConstraint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

BucketLocationConstraint: TypeAlias = Literal[
    "EU",
    "eu-west-1",
    "us-west-1",
    "us-west-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "sa-east-1",
    "cn-north-1",
    "eu-central-1",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EU",
        "eu-west-1",
        "us-west-1",
        "us-west-2",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "sa-east-1",
        "cn-north-1",
        "eu-central-1",
    )
)


def to_xml_text(value: BucketLocationConstraint) -> str:
    return value


def from_xml_text(text: str) -> BucketLocationConstraint:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketLocationConstraint value: {text!r}")
    return cast(BucketLocationConstraint, text)


def serialize_xml(value: BucketLocationConstraint, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketLocationConstraint:
    return from_xml_text(el.text or "")
