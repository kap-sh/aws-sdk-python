"""Generated from Smithy shape ``com.amazonaws.route53#ReusableDelegationSetLimitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

ReusableDelegationSetLimitType: TypeAlias = Literal[
    "MAX_ZONES_BY_REUSABLE_DELEGATION_SET",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(("MAX_ZONES_BY_REUSABLE_DELEGATION_SET",))


def to_xml_text(value: ReusableDelegationSetLimitType) -> str:
    return value


def from_xml_text(text: str) -> ReusableDelegationSetLimitType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ReusableDelegationSetLimitType value: {text!r}"
        )
    return cast(ReusableDelegationSetLimitType, text)


def serialize_xml(
    value: ReusableDelegationSetLimitType, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReusableDelegationSetLimitType:
    return from_xml_text(el.text or "")
