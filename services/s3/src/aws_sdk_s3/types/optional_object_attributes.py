"""Generated from Smithy shape ``com.amazonaws.s3#OptionalObjectAttributes``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

OptionalObjectAttributes: TypeAlias = Literal["RestoreStatus",]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("RestoreStatus",))


def to_xml_text(value: OptionalObjectAttributes) -> str:
    return value


def from_xml_text(text: str) -> OptionalObjectAttributes:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OptionalObjectAttributes value: {text!r}")
    return cast(OptionalObjectAttributes, text)


def serialize_xml(value: OptionalObjectAttributes, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OptionalObjectAttributes:
    return from_xml_text(el.text or "")
