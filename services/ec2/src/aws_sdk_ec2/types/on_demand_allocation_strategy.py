"""Generated from Smithy shape ``com.amazonaws.ec2#OnDemandAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

OnDemandAllocationStrategy: TypeAlias = Literal[
    "lowestPrice",
    "prioritized",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lowestPrice",
        "prioritized",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "lowestPrice",
        "prioritized",
    )
)


def to_ec2_query_text(value: OnDemandAllocationStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> OnDemandAllocationStrategy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown OnDemandAllocationStrategy value: {text!r}"
        )
    return cast(OnDemandAllocationStrategy, text)


def serialize_ec2_query(
    value: OnDemandAllocationStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OnDemandAllocationStrategy:
    return from_ec2_query_text(el.text or "")
