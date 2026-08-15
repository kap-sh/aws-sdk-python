"""Generated from Smithy shape ``com.amazonaws.ec2#FleetHttpTokensState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FleetHttpTokensState: TypeAlias = Literal[
    "optional",
    "required",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetHttpTokensState) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetHttpTokensState:
    return cast(FleetHttpTokensState, text)


def serialize_ec2_query(
    value: FleetHttpTokensState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetHttpTokensState:
    return from_ec2_query_text(el.text or "")
