"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityTenancy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityTenancy: TypeAlias = Literal[
    "default",
    "dedicated",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityTenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityTenancy:
    return cast(CapacityTenancy, text)


def serialize_ec2_query(
    value: CapacityTenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityTenancy:
    return from_ec2_query_text(el.text or "")
