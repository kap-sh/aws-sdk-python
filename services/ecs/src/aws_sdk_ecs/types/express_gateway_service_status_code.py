"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceStatusCode``."""

from typing import Literal, TypeAlias, cast

ExpressGatewayServiceStatusCode: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressGatewayServiceStatusCode:
    return cast(ExpressGatewayServiceStatusCode, data)
