"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationStrategy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

AllocationStrategy: TypeAlias = Literal[
    "lowestPrice",
    "diversified",
    "capacityOptimized",
    "capacityOptimizedPrioritized",
    "priceCapacityOptimized",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lowestPrice",
        "diversified",
        "capacityOptimized",
        "capacityOptimizedPrioritized",
        "priceCapacityOptimized",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "lowestPrice",
        "diversified",
        "capacityOptimized",
        "capacityOptimizedPrioritized",
        "priceCapacityOptimized",
    )
)


def to_ec2_query_text(value: AllocationStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> AllocationStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AllocationStrategy value: {text!r}")
    return cast(AllocationStrategy, text)


def serialize_ec2_query(
    value: AllocationStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AllocationStrategy:
    return from_ec2_query_text(el.text or "")
