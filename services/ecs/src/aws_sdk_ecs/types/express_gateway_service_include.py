"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceInclude``."""

from typing import Literal, TypeAlias, cast

ExpressGatewayServiceInclude: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceInclude) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressGatewayServiceInclude:
    return cast(ExpressGatewayServiceInclude, data)
