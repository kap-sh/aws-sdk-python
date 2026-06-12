"""Generated from Smithy shape ``com.amazonaws.s3control#OutputSchemaVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

OutputSchemaVersion: TypeAlias = Literal["V_1",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("V_1",))


def to_xml_text(value: OutputSchemaVersion) -> str:
    return value


def from_xml_text(text: str) -> OutputSchemaVersion:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OutputSchemaVersion value: {text!r}")
    return cast(OutputSchemaVersion, text)


def serialize_xml(value: OutputSchemaVersion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OutputSchemaVersion:
    return from_xml_text(el.text or "")
