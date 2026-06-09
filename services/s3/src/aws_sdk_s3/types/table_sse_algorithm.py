"""Generated from Smithy shape ``com.amazonaws.s3#TableSseAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

TableSseAlgorithm: TypeAlias = Literal[
    "aws:kms",
    "AES256",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aws:kms",
        "AES256",
    )
)


def to_xml_text(value: TableSseAlgorithm) -> str:
    return value


def from_xml_text(text: str) -> TableSseAlgorithm:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TableSseAlgorithm value: {text!r}")
    return cast(TableSseAlgorithm, text)


def serialize_xml(value: TableSseAlgorithm, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TableSseAlgorithm:
    return from_xml_text(el.text or "")
