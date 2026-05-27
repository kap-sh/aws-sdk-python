"""Generated from Smithy shape ``com.amazonaws.s3#ExpirationState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

ExpirationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def to_xml_text(value: ExpirationState) -> str:
    return value


def from_xml_text(text: str) -> ExpirationState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ExpirationState value: {text!r}")
    return cast(ExpirationState, text)


def serialize_xml(value: ExpirationState, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ExpirationState:
    return from_xml_text(el.text or "")
