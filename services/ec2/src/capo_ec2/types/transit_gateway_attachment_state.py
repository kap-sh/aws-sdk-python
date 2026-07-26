"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayAttachmentState: TypeAlias = Literal[
    "initiating",
    "initiatingRequest",
    "pendingAcceptance",
    "rollingBack",
    "pending",
    "available",
    "modifying",
    "deleting",
    "deleted",
    "failed",
    "rejected",
    "rejecting",
    "failing",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayAttachmentState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayAttachmentState:
    return cast(TransitGatewayAttachmentState, text)


def serialize_ec2_query(
    value: TransitGatewayAttachmentState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentState:
    return from_ec2_query_text(el.text or "")
