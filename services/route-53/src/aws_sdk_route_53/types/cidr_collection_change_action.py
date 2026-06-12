"""Generated from Smithy shape ``com.amazonaws.route53#CidrCollectionChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

CidrCollectionChangeAction: TypeAlias = Literal[
    "PUT",
    "DELETE_IF_EXISTS",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUT",
        "DELETE_IF_EXISTS",
    )
)


def to_xml_text(value: CidrCollectionChangeAction) -> str:
    return value


def from_xml_text(text: str) -> CidrCollectionChangeAction:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CidrCollectionChangeAction value: {text!r}"
        )
    return cast(CidrCollectionChangeAction, text)


def serialize_xml(value: CidrCollectionChangeAction, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CidrCollectionChangeAction:
    return from_xml_text(el.text or "")
