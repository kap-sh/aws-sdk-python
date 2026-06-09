"""Generated from Smithy shape ``com.amazonaws.s3#DataRedundancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

DataRedundancy: TypeAlias = Literal[
    "SingleAvailabilityZone",
    "SingleLocalZone",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SingleAvailabilityZone",
        "SingleLocalZone",
    )
)


def to_xml_text(value: DataRedundancy) -> str:
    return value


def from_xml_text(text: str) -> DataRedundancy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DataRedundancy value: {text!r}")
    return cast(DataRedundancy, text)


def serialize_xml(value: DataRedundancy, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DataRedundancy:
    return from_xml_text(el.text or "")
