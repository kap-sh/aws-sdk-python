"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ConnectPeerAssociationState: TypeAlias = Literal[
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


def serialize_json(value: ConnectPeerAssociationState) -> str:
    return value


def deserialize_json(data: str) -> ConnectPeerAssociationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConnectPeerAssociationState value: {data!r}"
        )
    return cast(ConnectPeerAssociationState, data)
