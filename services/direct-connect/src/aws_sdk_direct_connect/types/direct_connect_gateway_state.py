"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

DirectConnectGatewayState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


def serialize_aws_json_1_1(value: DirectConnectGatewayState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectConnectGatewayState value: {data!r}")
    return cast(DirectConnectGatewayState, data)
