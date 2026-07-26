"""Generated from Smithy shape ``com.amazonaws.storagegateway#GatewayCapacity``."""

from typing import Literal, TypeAlias, cast

GatewayCapacity: TypeAlias = Literal[
    "Small",
    "Medium",
    "Large",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayCapacity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GatewayCapacity:
    return cast(GatewayCapacity, data)
