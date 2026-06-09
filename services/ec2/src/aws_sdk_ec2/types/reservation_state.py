"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ReservationState: TypeAlias = Literal[
    "active",
    "expired",
    "cancelled",
    "scheduled",
    "pending",
    "failed",
    "delayed",
    "unsupported",
    "payment-pending",
    "payment-failed",
    "retired",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "expired",
        "cancelled",
        "scheduled",
        "pending",
        "failed",
        "delayed",
        "unsupported",
        "payment-pending",
        "payment-failed",
        "retired",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "expired",
        "cancelled",
        "scheduled",
        "pending",
        "failed",
        "delayed",
        "unsupported",
        "payment-pending",
        "payment-failed",
        "retired",
    )
)


def to_ec2_query_text(value: ReservationState) -> str:
    return value


def from_ec2_query_text(text: str) -> ReservationState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReservationState value: {text!r}")
    return cast(ReservationState, text)


def serialize_ec2_query(
    value: ReservationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReservationState:
    return from_ec2_query_text(el.text or "")
