"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ConnectPeerState: TypeAlias = Literal[
    "CREATING",
    "FAILED",
    "AVAILABLE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "FAILED",
        "AVAILABLE",
        "DELETING",
    )
)


def serialize_json(value: ConnectPeerState) -> str:
    return value


def deserialize_json(data: str) -> ConnectPeerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectPeerState value: {data!r}")
    return cast(ConnectPeerState, data)
