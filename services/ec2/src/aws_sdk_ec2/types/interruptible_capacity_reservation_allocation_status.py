"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptibleCapacityReservationAllocationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

InterruptibleCapacityReservationAllocationStatus: TypeAlias = Literal[
    "pending",
    "active",
    "updating",
    "canceling",
    "canceled",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "active",
        "updating",
        "canceling",
        "canceled",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "active",
        "updating",
        "canceling",
        "canceled",
        "failed",
    )
)


def to_ec2_query_text(value: InterruptibleCapacityReservationAllocationStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> InterruptibleCapacityReservationAllocationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InterruptibleCapacityReservationAllocationStatus value: {text!r}"
        )
    return cast(InterruptibleCapacityReservationAllocationStatus, text)


def serialize_ec2_query(
    value: InterruptibleCapacityReservationAllocationStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> InterruptibleCapacityReservationAllocationStatus:
    return from_ec2_query_text(el.text or "")
