"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ReservedInstanceState: TypeAlias = Literal[
    "payment-pending",
    "active",
    "payment-failed",
    "retired",
    "queued",
    "queued-deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "payment-pending",
        "active",
        "payment-failed",
        "retired",
        "queued",
        "queued-deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "payment-pending",
        "active",
        "payment-failed",
        "retired",
        "queued",
        "queued-deleted",
    )
)


def to_ec2_query_text(value: ReservedInstanceState) -> str:
    return value


def from_ec2_query_text(text: str) -> ReservedInstanceState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReservedInstanceState value: {text!r}")
    return cast(ReservedInstanceState, text)


def serialize_ec2_query(
    value: ReservedInstanceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReservedInstanceState:
    return from_ec2_query_text(el.text or "")
