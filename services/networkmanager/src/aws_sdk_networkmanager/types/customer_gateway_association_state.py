"""Generated from Smithy shape ``com.amazonaws.networkmanager#CustomerGatewayAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

CustomerGatewayAssociationState: TypeAlias = Literal[
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


def serialize_json(value: CustomerGatewayAssociationState) -> str:
    return value


def deserialize_json(data: str) -> CustomerGatewayAssociationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomerGatewayAssociationState value: {data!r}"
        )
    return cast(CustomerGatewayAssociationState, data)
