"""Generated from Smithy shape ``com.amazonaws.ec2#FleetType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FleetType: TypeAlias = Literal[
    "request",
    "maintain",
    "instant",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetType) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetType:
    return cast(FleetType, text)


def serialize_ec2_query(
    value: FleetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetType:
    return from_ec2_query_text(el.text or "")
