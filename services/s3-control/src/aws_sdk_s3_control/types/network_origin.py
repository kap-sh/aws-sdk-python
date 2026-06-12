"""Generated from Smithy shape ``com.amazonaws.s3control#NetworkOrigin``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

NetworkOrigin: TypeAlias = Literal[
    "Internet",
    "VPC",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Internet",
        "VPC",
    )
)


def to_xml_text(value: NetworkOrigin) -> str:
    return value


def from_xml_text(text: str) -> NetworkOrigin:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NetworkOrigin value: {text!r}")
    return cast(NetworkOrigin, text)


def serialize_xml(value: NetworkOrigin, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> NetworkOrigin:
    return from_xml_text(el.text or "")
