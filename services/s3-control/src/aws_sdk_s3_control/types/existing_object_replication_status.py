"""Generated from Smithy shape ``com.amazonaws.s3control#ExistingObjectReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

ExistingObjectReplicationStatus: TypeAlias = Literal[
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


def to_xml_text(value: ExistingObjectReplicationStatus) -> str:
    return value


def from_xml_text(text: str) -> ExistingObjectReplicationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ExistingObjectReplicationStatus value: {text!r}"
        )
    return cast(ExistingObjectReplicationStatus, text)


def serialize_xml(
    value: ExistingObjectReplicationStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ExistingObjectReplicationStatus:
    return from_xml_text(el.text or "")
