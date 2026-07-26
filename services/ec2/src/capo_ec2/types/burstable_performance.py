"""Generated from Smithy shape ``com.amazonaws.ec2#BurstablePerformance``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

BurstablePerformance: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: BurstablePerformance) -> str:
    return value


def from_ec2_query_text(text: str) -> BurstablePerformance:
    return cast(BurstablePerformance, text)


def serialize_ec2_query(
    value: BurstablePerformance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BurstablePerformance:
    return from_ec2_query_text(el.text or "")
