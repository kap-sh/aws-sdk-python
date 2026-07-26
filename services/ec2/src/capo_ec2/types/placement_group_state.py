"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

PlacementGroupState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PlacementGroupState) -> str:
    return value


def from_ec2_query_text(text: str) -> PlacementGroupState:
    return cast(PlacementGroupState, text)


def serialize_ec2_query(
    value: PlacementGroupState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PlacementGroupState:
    return from_ec2_query_text(el.text or "")
