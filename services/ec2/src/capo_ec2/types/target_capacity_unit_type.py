"""Generated from Smithy shape ``com.amazonaws.ec2#TargetCapacityUnitType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TargetCapacityUnitType: TypeAlias = Literal[
    "vcpu",
    "memory-mib",
    "units",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TargetCapacityUnitType) -> str:
    return value


def from_ec2_query_text(text: str) -> TargetCapacityUnitType:
    return cast(TargetCapacityUnitType, text)


def serialize_ec2_query(
    value: TargetCapacityUnitType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TargetCapacityUnitType:
    return from_ec2_query_text(el.text or "")
