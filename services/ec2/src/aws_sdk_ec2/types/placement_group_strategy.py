"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupStrategy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

PlacementGroupStrategy: TypeAlias = Literal[
    "cluster",
    "partition",
    "spread",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cluster",
        "partition",
        "spread",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "cluster",
        "partition",
        "spread",
    )
)


def to_ec2_query_text(value: PlacementGroupStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> PlacementGroupStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PlacementGroupStrategy value: {text!r}")
    return cast(PlacementGroupStrategy, text)


def serialize_ec2_query(
    value: PlacementGroupStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PlacementGroupStrategy:
    return from_ec2_query_text(el.text or "")
