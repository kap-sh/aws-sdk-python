"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayConnectPeerAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

TransitGatewayConnectPeerAssociationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: TransitGatewayConnectPeerAssociationState) -> str:
    return value


def deserialize_json(data: str) -> TransitGatewayConnectPeerAssociationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayConnectPeerAssociationState value: {data!r}"
        )
    return cast(TransitGatewayConnectPeerAssociationState, data)
