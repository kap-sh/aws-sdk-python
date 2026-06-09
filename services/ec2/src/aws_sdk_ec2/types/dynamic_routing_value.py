"""Generated from Smithy shape ``com.amazonaws.ec2#DynamicRoutingValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DynamicRoutingValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


def to_ec2_query_text(value: DynamicRoutingValue) -> str:
    return value


def from_ec2_query_text(text: str) -> DynamicRoutingValue:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DynamicRoutingValue value: {text!r}")
    return cast(DynamicRoutingValue, text)


def serialize_ec2_query(
    value: DynamicRoutingValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DynamicRoutingValue:
    return from_ec2_query_text(el.text or "")
