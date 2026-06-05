"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementStrategy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

PlacementStrategy: TypeAlias = Literal[
    "cluster",
    "spread",
    "partition",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cluster",
        "spread",
        "partition",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "cluster",
        "spread",
        "partition",
    )
)


def to_ec2_query_text(value: PlacementStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> PlacementStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PlacementStrategy value: {text!r}")
    return cast(PlacementStrategy, text)


def serialize_ec2_query(
    value: PlacementStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PlacementStrategy:
    return from_ec2_query_text(el.text or "")
