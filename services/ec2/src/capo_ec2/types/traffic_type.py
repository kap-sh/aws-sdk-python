"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TrafficType: TypeAlias = Literal[
    "ACCEPT",
    "REJECT",
    "ALL",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TrafficType) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficType:
    return cast(TrafficType, text)


def serialize_ec2_query(
    value: TrafficType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficType:
    return from_ec2_query_text(el.text or "")
