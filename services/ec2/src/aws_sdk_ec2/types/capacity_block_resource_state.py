"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockResourceState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

CapacityBlockResourceState: TypeAlias = Literal[
    "active",
    "expired",
    "unavailable",
    "cancelled",
    "failed",
    "scheduled",
    "payment-pending",
    "payment-failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "expired",
        "unavailable",
        "cancelled",
        "failed",
        "scheduled",
        "payment-pending",
        "payment-failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "expired",
        "unavailable",
        "cancelled",
        "failed",
        "scheduled",
        "payment-pending",
        "payment-failed",
    )
)


def to_ec2_query_text(value: CapacityBlockResourceState) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityBlockResourceState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityBlockResourceState value: {text!r}"
        )
    return cast(CapacityBlockResourceState, text)


def serialize_ec2_query(
    value: CapacityBlockResourceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityBlockResourceState:
    return from_ec2_query_text(el.text or "")
