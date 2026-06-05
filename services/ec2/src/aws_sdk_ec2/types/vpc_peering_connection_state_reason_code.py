"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionStateReasonCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VpcPeeringConnectionStateReasonCode: TypeAlias = Literal[
    "initiating-request",
    "pending-acceptance",
    "active",
    "deleted",
    "rejected",
    "failed",
    "expired",
    "provisioning",
    "deleting",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "initiating-request",
        "pending-acceptance",
        "active",
        "deleted",
        "rejected",
        "failed",
        "expired",
        "provisioning",
        "deleting",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "initiating-request",
        "pending-acceptance",
        "active",
        "deleted",
        "rejected",
        "failed",
        "expired",
        "provisioning",
        "deleting",
    )
)


def to_ec2_query_text(value: VpcPeeringConnectionStateReasonCode) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcPeeringConnectionStateReasonCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown VpcPeeringConnectionStateReasonCode value: {text!r}"
        )
    return cast(VpcPeeringConnectionStateReasonCode, text)


def serialize_ec2_query(
    value: VpcPeeringConnectionStateReasonCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcPeeringConnectionStateReasonCode:
    return from_ec2_query_text(el.text or "")
