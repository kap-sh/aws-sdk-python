"""Generated from Smithy shape ``com.amazonaws.gamelift#RoutingStrategyType``."""

from typing import Literal, TypeAlias, cast

RoutingStrategyType: TypeAlias = Literal[
    "SIMPLE",
    "TERMINAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingStrategyType:
    return cast(RoutingStrategyType, data)
