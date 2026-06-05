"""Generated from Smithy shape ``com.amazonaws.ec2#FleetReplacementStrategy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

FleetReplacementStrategy: TypeAlias = Literal[
    "launch",
    "launch-before-terminate",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "launch",
        "launch-before-terminate",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "launch",
        "launch-before-terminate",
    )
)


def to_ec2_query_text(value: FleetReplacementStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetReplacementStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FleetReplacementStrategy value: {text!r}")
    return cast(FleetReplacementStrategy, text)


def serialize_ec2_query(
    value: FleetReplacementStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetReplacementStrategy:
    return from_ec2_query_text(el.text or "")
