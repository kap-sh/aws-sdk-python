"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficRoutingConfigType``."""

from typing import Literal, TypeAlias, cast

TrafficRoutingConfigType: TypeAlias = Literal[
    "ALL_AT_ONCE",
    "CANARY",
    "LINEAR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficRoutingConfigType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrafficRoutingConfigType:
    return cast(TrafficRoutingConfigType, data)
