"""Generated from Smithy shape ``com.amazonaws.s3#MFADeleteStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

MFADeleteStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_xml_text(value: MFADeleteStatus) -> str:
    return value


def from_xml_text(text: str) -> MFADeleteStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MFADeleteStatus value: {text!r}")
    return cast(MFADeleteStatus, text)


def serialize_xml(value: MFADeleteStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MFADeleteStatus:
    return from_xml_text(el.text or "")
