"""Generated from Smithy shape ``com.amazonaws.directconnect#GatewayType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

GatewayType: TypeAlias = Literal[
    "virtualPrivateGateway",
    "transitGateway",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "virtualPrivateGateway",
        "transitGateway",
    )
)


def serialize_aws_json_1_1(value: GatewayType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayType value: {data!r}")
    return cast(GatewayType, data)
