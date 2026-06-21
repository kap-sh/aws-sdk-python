"""Generated from Smithy shape ``com.amazonaws.directconnect#GatewayType``."""

from typing import Literal, TypeAlias, cast

GatewayType: TypeAlias = Literal[
    "virtualPrivateGateway",
    "transitGateway",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayType:
    return cast(GatewayType, data)
