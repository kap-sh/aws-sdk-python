"""Generated from Smithy shape ``com.amazonaws.s3#BucketNamespace``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

BucketNamespace: TypeAlias = Literal[
    "account-regional",
    "global",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "account-regional",
        "global",
    )
)


def to_xml_text(value: BucketNamespace) -> str:
    return value


def from_xml_text(text: str) -> BucketNamespace:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BucketNamespace value: {text!r}")
    return cast(BucketNamespace, text)


def serialize_xml(value: BucketNamespace, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> BucketNamespace:
    return from_xml_text(el.text or "")
