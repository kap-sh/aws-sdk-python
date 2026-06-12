"""Generated from Smithy shape ``com.amazonaws.s3control#TransitionStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

TransitionStorageClass: TypeAlias = Literal[
    "GLACIER",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "DEEP_ARCHIVE",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GLACIER",
        "STANDARD_IA",
        "ONEZONE_IA",
        "INTELLIGENT_TIERING",
        "DEEP_ARCHIVE",
    )
)


def to_xml_text(value: TransitionStorageClass) -> str:
    return value


def from_xml_text(text: str) -> TransitionStorageClass:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TransitionStorageClass value: {text!r}")
    return cast(TransitionStorageClass, text)


def serialize_xml(value: TransitionStorageClass, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TransitionStorageClass:
    return from_xml_text(el.text or "")
