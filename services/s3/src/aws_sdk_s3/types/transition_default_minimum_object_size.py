"""Generated from Smithy shape ``com.amazonaws.s3#TransitionDefaultMinimumObjectSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

TransitionDefaultMinimumObjectSize: TypeAlias = Literal[
    "varies_by_storage_class",
    "all_storage_classes_128K",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "varies_by_storage_class",
        "all_storage_classes_128K",
    )
)


def to_xml_text(value: TransitionDefaultMinimumObjectSize) -> str:
    return value


def from_xml_text(text: str) -> TransitionDefaultMinimumObjectSize:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitionDefaultMinimumObjectSize value: {text!r}"
        )
    return cast(TransitionDefaultMinimumObjectSize, text)


def serialize_xml(
    value: TransitionDefaultMinimumObjectSize, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TransitionDefaultMinimumObjectSize:
    return from_xml_text(el.text or "")
