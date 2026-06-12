"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

DirectConnectGatewayAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "updating",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "disassociating",
        "disassociated",
        "updating",
    )
)


def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAssociationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectConnectGatewayAssociationState value: {data!r}"
        )
    return cast(DirectConnectGatewayAssociationState, data)
