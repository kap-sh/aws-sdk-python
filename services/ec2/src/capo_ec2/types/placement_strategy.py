"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementStrategy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

PlacementStrategy: TypeAlias = Literal[
    "cluster",
    "spread",
    "partition",
    "precision-time",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PlacementStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> PlacementStrategy:
    return cast(PlacementStrategy, text)


def serialize_ec2_query(
    value: PlacementStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PlacementStrategy:
    return from_ec2_query_text(el.text or "")
