"""Generated from Smithy shape ``com.amazonaws.route53#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

ChangeAction: TypeAlias = Literal[
    "CREATE",
    "DELETE",
    "UPSERT",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "DELETE",
        "UPSERT",
    )
)


def to_xml_text(value: ChangeAction) -> str:
    return value


def from_xml_text(text: str) -> ChangeAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChangeAction value: {text!r}")
    return cast(ChangeAction, text)


def serialize_xml(value: ChangeAction, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChangeAction:
    return from_xml_text(el.text or "")
