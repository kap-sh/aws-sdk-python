"""Generated from Smithy shape ``com.amazonaws.route53#ChangeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

ChangeStatus: TypeAlias = Literal[
    "PENDING",
    "INSYNC",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "INSYNC",
    )
)


def to_xml_text(value: ChangeStatus) -> str:
    return value


def from_xml_text(text: str) -> ChangeStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChangeStatus value: {text!r}")
    return cast(ChangeStatus, text)


def serialize_xml(value: ChangeStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChangeStatus:
    return from_xml_text(el.text or "")
