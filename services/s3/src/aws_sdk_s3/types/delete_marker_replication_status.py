"""Generated from Smithy shape ``com.amazonaws.s3#DeleteMarkerReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

DeleteMarkerReplicationStatus: TypeAlias = Literal[
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


def to_xml_text(value: DeleteMarkerReplicationStatus) -> str:
    return value


def from_xml_text(text: str) -> DeleteMarkerReplicationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown DeleteMarkerReplicationStatus value: {text!r}"
        )
    return cast(DeleteMarkerReplicationStatus, text)


def serialize_xml(
    value: DeleteMarkerReplicationStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DeleteMarkerReplicationStatus:
    return from_xml_text(el.text or "")
