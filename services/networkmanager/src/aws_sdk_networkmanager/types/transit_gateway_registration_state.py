"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRegistrationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

TransitGatewayRegistrationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "DELETED",
        "FAILED",
    )
)


def serialize_json(value: TransitGatewayRegistrationState) -> str:
    return value


def deserialize_json(data: str) -> TransitGatewayRegistrationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayRegistrationState value: {data!r}"
        )
    return cast(TransitGatewayRegistrationState, data)
