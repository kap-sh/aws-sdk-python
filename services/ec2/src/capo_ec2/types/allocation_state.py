"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AllocationState: TypeAlias = Literal[
    "available",
    "under-assessment",
    "permanent-failure",
    "released",
    "released-permanent-failure",
    "pending",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AllocationState) -> str:
    return value


def from_ec2_query_text(text: str) -> AllocationState:
    return cast(AllocationState, text)


def serialize_ec2_query(
    value: AllocationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AllocationState:
    return from_ec2_query_text(el.text or "")
