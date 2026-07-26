"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionStateReasonCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

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
def to_ec2_query_text(value: VpcPeeringConnectionStateReasonCode) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcPeeringConnectionStateReasonCode:
    return cast(VpcPeeringConnectionStateReasonCode, text)


def serialize_ec2_query(
    value: VpcPeeringConnectionStateReasonCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcPeeringConnectionStateReasonCode:
    return from_ec2_query_text(el.text or "")
