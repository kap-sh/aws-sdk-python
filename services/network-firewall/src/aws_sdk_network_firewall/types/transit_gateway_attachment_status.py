"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TransitGatewayAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

TransitGatewayAttachmentStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "DELETED",
    "FAILED",
    "ERROR",
    "READY",
    "PENDING_ACCEPTANCE",
    "REJECTING",
    "REJECTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "DELETED",
        "FAILED",
        "ERROR",
        "READY",
        "PENDING_ACCEPTANCE",
        "REJECTING",
        "REJECTED",
    )
)


def serialize_aws_json_1_0(value: TransitGatewayAttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransitGatewayAttachmentStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayAttachmentStatus value: {data!r}"
        )
    return cast(TransitGatewayAttachmentStatus, data)
