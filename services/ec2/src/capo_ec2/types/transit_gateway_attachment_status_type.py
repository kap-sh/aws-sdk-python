"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentStatusType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayAttachmentStatusType: TypeAlias = Literal[
    "pending-acceptance",
    "pending",
    "rejected",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayAttachmentStatusType) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayAttachmentStatusType:
    return cast(TransitGatewayAttachmentStatusType, text)


def serialize_ec2_query(
    value: TransitGatewayAttachmentStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentStatusType:
    return from_ec2_query_text(el.text or "")
