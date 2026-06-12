"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

PeeringErrorCode: TypeAlias = Literal[
    "TRANSIT_GATEWAY_NOT_FOUND",
    "TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED",
    "MISSING_PERMISSIONS",
    "INTERNAL_ERROR",
    "EDGE_LOCATION_PEER_DUPLICATE",
    "INVALID_TRANSIT_GATEWAY_STATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRANSIT_GATEWAY_NOT_FOUND",
        "TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED",
        "MISSING_PERMISSIONS",
        "INTERNAL_ERROR",
        "EDGE_LOCATION_PEER_DUPLICATE",
        "INVALID_TRANSIT_GATEWAY_STATE",
    )
)


def serialize_json(value: PeeringErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PeeringErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeeringErrorCode value: {data!r}")
    return cast(PeeringErrorCode, data)
