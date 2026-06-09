"""Generated from Smithy shape ``com.amazonaws.ec2#DefaultTargetCapacityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DefaultTargetCapacityType: TypeAlias = Literal[
    "spot",
    "on-demand",
    "capacity-block",
    "reserved-capacity",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "on-demand",
        "capacity-block",
        "reserved-capacity",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "on-demand",
        "capacity-block",
        "reserved-capacity",
    )
)


def to_ec2_query_text(value: DefaultTargetCapacityType) -> str:
    return value


def from_ec2_query_text(text: str) -> DefaultTargetCapacityType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DefaultTargetCapacityType value: {text!r}")
    return cast(DefaultTargetCapacityType, text)


def serialize_ec2_query(
    value: DefaultTargetCapacityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DefaultTargetCapacityType:
    return from_ec2_query_text(el.text or "")
