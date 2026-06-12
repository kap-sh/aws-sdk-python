"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

MultiRegionAccessPointStatus: TypeAlias = Literal[
    "READY",
    "INCONSISTENT_ACROSS_REGIONS",
    "CREATING",
    "PARTIALLY_CREATED",
    "PARTIALLY_DELETED",
    "DELETING",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "INCONSISTENT_ACROSS_REGIONS",
        "CREATING",
        "PARTIALLY_CREATED",
        "PARTIALLY_DELETED",
        "DELETING",
    )
)


def to_xml_text(value: MultiRegionAccessPointStatus) -> str:
    return value


def from_xml_text(text: str) -> MultiRegionAccessPointStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown MultiRegionAccessPointStatus value: {text!r}"
        )
    return cast(MultiRegionAccessPointStatus, text)


def serialize_xml(
    value: MultiRegionAccessPointStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MultiRegionAccessPointStatus:
    return from_xml_text(el.text or "")
