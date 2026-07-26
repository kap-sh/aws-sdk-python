"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AvailabilityZoneState: TypeAlias = Literal[
    "available",
    "information",
    "impaired",
    "unavailable",
    "constrained",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AvailabilityZoneState) -> str:
    return value


def from_ec2_query_text(text: str) -> AvailabilityZoneState:
    return cast(AvailabilityZoneState, text)


def serialize_ec2_query(
    value: AvailabilityZoneState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AvailabilityZoneState:
    return from_ec2_query_text(el.text or "")
