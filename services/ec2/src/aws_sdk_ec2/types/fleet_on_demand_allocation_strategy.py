"""Generated from Smithy shape ``com.amazonaws.ec2#FleetOnDemandAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

FleetOnDemandAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "prioritized",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lowest-price",
        "prioritized",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "lowest-price",
        "prioritized",
    )
)


def to_ec2_query_text(value: FleetOnDemandAllocationStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetOnDemandAllocationStrategy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown FleetOnDemandAllocationStrategy value: {text!r}"
        )
    return cast(FleetOnDemandAllocationStrategy, text)


def serialize_ec2_query(
    value: FleetOnDemandAllocationStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetOnDemandAllocationStrategy:
    return from_ec2_query_text(el.text or "")
