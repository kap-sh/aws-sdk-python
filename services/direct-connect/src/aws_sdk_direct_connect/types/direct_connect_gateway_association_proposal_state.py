"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationProposalState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

DirectConnectGatewayAssociationProposalState: TypeAlias = Literal[
    "requested",
    "accepted",
    "deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "requested",
        "accepted",
        "deleted",
    )
)


def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationProposalState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAssociationProposalState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectConnectGatewayAssociationProposalState value: {data!r}"
        )
    return cast(DirectConnectGatewayAssociationProposalState, data)
